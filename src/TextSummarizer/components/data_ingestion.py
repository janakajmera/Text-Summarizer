import os
import urllib.request as request
from pathlib import Path
import zipfile
from src.TextSummarizer.logging import logger
from src.TextSummarizer.utils.common import get_size
from src.TextSummarizer.entity import DataIngestionConfig
#     Returns the size of a file or directory.

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Download file from URL and save it locally
        """

        logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") 


    def extract_zip_file(self):
        """
        Extract zip file to the specified directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to: {unzip_path}")