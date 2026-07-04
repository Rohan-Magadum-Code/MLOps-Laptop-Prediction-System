from Laptop_Price_Prediction_System import logger
from Laptop_Price_Prediction_System.pipeline.stage_01_data_ingestion import DataIngestionPipeline

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