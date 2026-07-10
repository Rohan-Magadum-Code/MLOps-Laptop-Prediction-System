from pathlib import Path
from Laptop_Price_Prediction_System.config.configuration import ConfigurationManager
from Laptop_Price_Prediction_System.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as file:
                status = file.read().split(" ")[-1].strip()
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.transform()
                data_transformation.create_preprocessor()
        except Exception as e:
            raise e