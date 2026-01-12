from Yes_Bank.logging import logger     
from Yes_Bank.exception.exception import YesBankException
import sys
from Yes_Bank.entity.config_entity import TrainingPipelineConfig
from Yes_Bank.entity.config_entity import DataIngestionConfig
from Yes_Bank.components.data_ingestion import DataIngestion
from Yes_Bank.entity.artifact_entity import DataIngestionArtifact
from Yes_Bank.entity.config_entity import DataTransformationConfig
from Yes_Bank.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        #data ingestion
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        dataingestionartifact= data_ingestion.initiate_data_ingestion()
        logger.logging.info("Data Ingestion completed successfully")

        # Data transformation
        data_transformation_config = DataTransformationConfig(training_pipeline_config)

        data_transformation = DataTransformation(dataingestionartifact, data_transformation_config)

        data_transformation.initiate_data_transformation()
        logger.logging.info("Data Transformation completed successfully")


        
    except Exception as e:
        raise YesBankException(e, sys)