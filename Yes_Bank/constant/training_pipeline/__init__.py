import os

# name of the project
PIPELINE_NAME = "YesBankPipeline"

# main folder where all outputs will be saved
ARTIFACT_DIR = "artifacts"

# dataset details
DATA_FILE_NAME = "data_YesBank_StockPrices.csv"
DATA_DIR = "data"

# data ingestion
RAW_DATA_PATH= "raw_data.csv"
TRAINING_PATH = "train.csv"
TESTING_PATH = "test.csv"
RAW_DATA_DIR = "raw_data"


# data ingestion directry
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
#DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

# preprocessing
DATA_PREPROCESSING_DIR = "data_preprocessing"
PROCESSED_DATA_DIR = "processed_data"
