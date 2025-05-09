# COnfiguration file for the Text Summarizer project

from src.TextSummarizer.constants import *
from src.TextSummarizer.utils.common import read_yaml, create_directories
from src.TextSummarizer.logging import logger
from src.TextSummarizer.entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath: str = CONFIG_FILE_PATH,
            params_filepath: str = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        logger.info(f"Data Ingestion config: {data_ingestion_config.root_dir} , {data_ingestion_config.source_URL} , {data_ingestion_config.local_data_file} , {data_ingestion_config.unzip_dir}")
        
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
