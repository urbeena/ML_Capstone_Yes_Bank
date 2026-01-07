from Yes_Bank.logging import logger     
from Yes_Bank.exception.exception import YesBankException
import sys
from Yes_Bank.entity.config_entity import TrainingPipelineConfig
from Yes_Bank.entity.config_entity import DataIngestionConfig
from Yes_Bank.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        dataingestionartifact= data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

        logger.logging.info("Data Ingestion completed successfully")


        
    except Exception as e:
        raise YesBankException(e, sys)