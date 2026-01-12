import pandas as pd
from Yes_Bank.logging import logger   
from Yes_Bank.exception.exception import YesBankException
import sys  
from Yes_Bank.entity.config_entity import DataIngestionConfig
import os
import numpy as np
from sklearn.model_selection import train_test_split
from Yes_Bank.entity.artifact_entity import DataIngestionArtifact
file_path = "data/data_YesBank_StockPrices.csv"

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise YesBankException(e,sys)
        
    def read_data_into_ingested_folder(self):
        try:

            df=pd.read_csv(file_path)
            logger.logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True) 
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logger.logging.info("Saved the raw data")
            df.replace("na",np.nan,inplace=True)
            return df

            
        except Exception as e:
            raise YesBankException(e,sys)
        
    
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        '''take data from feature store and split into train and test file
        and save them into ingested folder'''
        try:
            train_set,test_set= train_test_split(dataframe, test_size=0.2, random_state=42)

            logger.logging.info("Performed train test split on the dataframe")

            logger.logging.info("Exited split_data_as_train_test method of Data Ingestion class")

            dir_path= os.path.dirname(self.data_ingestion_config.train_data_path)
            os.makedirs(dir_path,exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logger.logging.info("Saved the train and test data into ingested folder")

            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logger.logging.info(f"Exported train and test file path")


        except Exception as e:
            raise YesBankException(e,sys)
        

    def initiate_data_ingestion(self):
        try:
           dataframe= self.read_data_into_ingested_folder()
           self.split_data_as_train_test(dataframe=dataframe)

           data_ingestion_artifact=DataIngestionArtifact(
               train_path = self.data_ingestion_config.train_data_path,
               test_path= self.data_ingestion_config.test_data_path
           )
           logger.logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}")

           return data_ingestion_artifact
           
        except Exception as e:
            raise YesBankException(e,sys)
    
