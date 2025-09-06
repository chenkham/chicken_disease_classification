import os
import urllib.request as request
import zipfile
import py7zr
from Chicken_disease_classification import logger
from Chicken_disease_classification.utils.common import get_size
from Chicken_disease_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        # For .7z extraction
        if self.config.local_data_file.endswith(".7z"):
            with py7zr.SevenZipFile(self.config.local_data_file, mode="r") as archive:
                archive.extractall(path=unzip_path)
            print(f"✅ Extracted .7z to {unzip_path}")

        # Optional: if you also want to handle .zip in future
        elif self.config.local_data_file.endswith(".zip"):
            import zipfile
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            print(f"✅ Extracted .zip to {unzip_path}")

        else:
            raise ValueError("Unsupported file type for extraction")