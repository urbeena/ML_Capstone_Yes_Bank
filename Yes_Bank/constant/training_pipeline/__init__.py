
PIPELINE_NAME= 'YesBank'
ARTIFACT_DIR= 'artifacts'


# dataset details
DATA_FILE_NAME = "data_YesBank_StockPrices.csv"
DATA_DIR = "data"

# data ingestion
RAW_DATA_PATH= "raw_data.csv"
TRAINING_PATH = "train.csv"
TESTING_PATH = "test.csv"

# data ingestion directry
DATA_INGESTION_DIR_NAME: str = "data_ingestion"



#Data Transformation
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"


DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"

preprocessor_obj = 'preprocessor_obj.pkl'