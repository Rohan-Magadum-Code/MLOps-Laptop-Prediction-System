from pathlib import Path
from Laptop_Price_Prediction_System.config.configuration import ConfigurationManager
from Laptop_Price_Prediction_System.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluation()
        except Exception as e:
            raise e