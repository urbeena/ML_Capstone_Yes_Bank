from Yes_Bank.logging import logger     
from Yes_Bank.exception.exception import YesBankException
import sys
from Yes_Bank.entity.config_entity import TrainingPipelineConfig
from Yes_Bank.entity.config_entity import DataIngestionConfig
from Yes_Bank.components.data_ingestion import DataIngestion

from Yes_Bank.entity.artifact_entity import DataIngestionArtifact
from Yes_Bank.entity.config_entity import DataTransformationConfig
from Yes_Bank.components.data_transformation import DataTransformation

from Yes_Bank.entity.config_entity import ModelTrainerConfig
from Yes_Bank.components.model_train import ModelTrainer

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

        DataTransformationArtifact=data_transformation.initiate_data_transformation()
        logger.logging.info("Data Transformation completed successfully")

        # Model Trainer
        model_trainer_config= ModelTrainerConfig(training_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config,DataTransformationArtifact)
        model_trainer_artifact= model_trainer.initiate_model_trainer()
        logger.logging.info("Model Training completed successfully")


        
    except Exception as e:
        raise YesBankException(e, sys)