from Laptop_Price_Prediction_System import logger
from Laptop_Price_Prediction_System.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from Laptop_Price_Prediction_System.pipeline.stage_02_data_validation import DataValidationPipeline

Stage_Name = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>> {Stage_Name} Started! <<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>> {Stage_Name} Finished! <<<")
    except Exception as e:
        logger.exception(e)
        raise e

Stage_Name = "Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>> {Stage_Name} Started! <<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>> {Stage_Name} Finished! <<<")
    except Exception as e:
        logger.exception(e)
        raise e