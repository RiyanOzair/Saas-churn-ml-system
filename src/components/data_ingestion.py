import os 
import sys
import pandas as pd

from src.exception import CustomException
from src.constants import RAW_DATA_PATH, PROCESSED_DATA_DIR
from src.logger import logging

class DataIngestion:
    def __init__(self):
        self.raw_data_path = RAW_DATA_PATH
        self.processed_data_dir = PROCESSED_DATA_DIR
    def load_data(self):
        try:
            logging.info("Loading raw data from path: %s", self.raw_data_path)
            data = pd.read_csv(self.raw_data_path)
            logging.info("Data loaded successfully with shape: %s", data.shape)
            os.makedirs(self.processed_data_dir, exist_ok=True)
            output_path = os.path.join(self.processed_data_dir, "raw_loaded.csv")
            data.to_csv(output_path, index=False)
            logging.info("Raw data saved to processed folder")
            return data
        except Exception as e:
            logging.error("Error occurred while loading data: %s", str(e))
            raise CustomException(e, sys)