import pandas as pd
import os
from Laptop_Price_Prediction_System import logger
from sklearn.ensemble import RandomForestRegressor
import joblib
from Laptop_Price_Prediction_System.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        logger.info("Loading Training Data")
        train_data = pd.read_csv(self.config.train_data_path)

        logger.info("Loading Preprocessor")
        preprocessor = joblib.load(self.config.preprocessor_obj_file_path)

        train_X = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]

        X_processed = preprocessor.transform(train_X)

        logger.info("Training Model")
        model = RandomForestRegressor(n_estimators=self.config.n_estimators, max_depth=self.config.max_depth, min_samples_split=self.config.min_samples_split, min_samples_leaf=self.config.min_samples_leaf)
        model.fit(X_processed, train_y)
        
        logger.info("Saving Model")
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))