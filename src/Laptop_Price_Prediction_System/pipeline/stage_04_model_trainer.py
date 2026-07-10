from pathlib import Path
from Laptop_Price_Prediction_System.config.configuration import ConfigurationManager
from Laptop_Price_Prediction_System.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e