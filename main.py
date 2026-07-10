from Laptop_Price_Prediction_System import logger
from Laptop_Price_Prediction_System.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Laptop_Price_Prediction_System.pipeline.stage_02_data_validation import DataValidationPipeline
from Laptop_Price_Prediction_System.pipeline.stage_03_data_transformation import DataTransformationPipeline
from Laptop_Price_Prediction_System.pipeline.stage_04_model_trainer import ModelTrainerPipeline

Stage_Name = "Data Ingestion Stage"
try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Validation Stage"
try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.exception(e)
    raise e
    
Stage_Name = "Data Transformation Stage"
try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Training Stage"
try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.exception(e)
    raise e