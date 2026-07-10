import numpy as np
import pandas as pd
from pathlib import Path
from Laptop_Price_Prediction_System import logger
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from Laptop_Price_Prediction_System.entity.config_entity import ModelEvaluationConfig
from Laptop_Price_Prediction_System.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def evaluation(self):
        test_data = pd.read_csv(self.config.test_data_path)

        preprocessor = joblib.load(self.config.preprocessor)
        model = joblib.load(self.config.model_path)


        test_X = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        X_preprocessor = preprocessor.transform(test_X)

        predicted_qualities = model.predict(X_preprocessor)

        logger.info("Starting Model Evaluation")
        rmse, mae, r2_score = self.eval_metrics(test_y, predicted_qualities)

        scores = {"rmse": rmse, "mae": mae, "r2_score": r2_score}
        save_json(path=Path(self.config.metric_file_name), data=scores)