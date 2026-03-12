import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException

class DataValidation:
    def __init__(self,df: pd.DataFrame):
        self.df = df

    def validate_columns(self):
        expected_columns =[
            "customerID",
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges",
            "Churn"
        ]

        missing_columns = set(expected_columns) - set(self.df.columns)

        if missing_columns:
            logging.error(f"Missing columns: {missing_columns}")
        logging.info("Column validation successful. All expected columns are present.")

    def check_missing_values(self):
        missing_values = self.df.isnull().sum()
        if missing_values.any():
            logging.error(f"Missing values found: {missing_values[missing_values > 0]}")
        logging.info("Missing value validation successful. No missing values found.")

    def check_duplicates(self):
        duplicate_count = self.df.duplicated().sum()
        if duplicate_count > 0:
            logging.error(f"Duplicate records found: {duplicate_count}")
        logging.info("Duplicate record validation successful. No duplicate records found.")

    def validate_data_types(self):
        expected_data_types = {
            "customerID": object,
            "gender": object,
            "SeniorCitizen": int,
            "Partner": object,
            "Dependents": object,
            "tenure": int,
            "PhoneService": object,
            "MultipleLines": object,
            "InternetService": object,
            "OnlineSecurity": object,
            "OnlineBackup": object,
            "DeviceProtection": object,
            "TechSupport": object,
            "StreamingTV": object,
            "StreamingMovies": object,
            "Contract": object,
            "PaperlessBilling": object,
            "PaymentMethod": object,
            "MonthlyCharges": float,
            "TotalCharges": object,
            "Churn": object
        }
        for column, expected_type in expected_data_types.items():
            if column in self.df.columns:
                actual_type = self.df[column].dtype
                if actual_type != expected_type:
                    logging.error(f"Data type mismatch for column '{column}': expected {expected_type}, got {actual_type}")
        logging.info("Data type validation successful. All columns have expected data types.")

    def validate(self):
        try:
            logging.info("Starting data validation.")
            self.validate_columns()
            self.check_missing_values()
            self.check_duplicates()
            self.validate_data_types()
            logging.info("Data validation completed successfully.")
        except Exception as e:
            logging.error(f"Data validation failed: {e}")
            raise CustomException(f"Data validation failed: {e}", sys)
    