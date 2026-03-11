import os 

# This file contains all the constant variables that are used in the project.
ROOT_DIR = os.getcwd()


# Define the path to the raw data file (Original dataset)
RAW_DATA_PATH = os.path.join(
    ROOT_DIR,
    "data",
    "raw",
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

PROCESSED_DATA_DIR = os.path.join(
    ROOT_DIR,
    "data",
    "processed"
)

ARTIFACT_DIR = os.path.join(ROOT_DIR, "artifacts")

MODEL_DIR = os.path.join(ARTIFACT_DIR, "models")

MODEL_FILE_NAME = "churn_model.pkl"

CONFIG_FILE_PATH = os.path.join(
    ROOT_DIR,
    "configs",
    "config.yaml"
)

