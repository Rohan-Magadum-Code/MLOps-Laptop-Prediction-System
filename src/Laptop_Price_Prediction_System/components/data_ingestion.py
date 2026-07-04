import os
from pathlib import Path
import urllib.request as request
import zipfile
from Laptop_Price_Prediction_System import logger
from Laptop_Price_Prediction_System.utils.common import get_size
from Laptop_Price_Prediction_System.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename}")
        else:
            logger.info(f"File Already Exists: {get_size(Path(self.config.local_file_data))}")
    
    def extract_zip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)