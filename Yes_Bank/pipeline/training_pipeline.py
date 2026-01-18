from Yes_Bank.logging import logger     
from Yes_Bank.exception.exception import YesBankException
import sys
from Yes_Bank.entity.config_entity import TrainingPipelineConfig
from Yes_Bank.entity.config_entity import DataIngestionConfig
from Yes_Bank.components.data_ingestion import DataIngestion

from Yes_Bank.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, ModelTrainerArtifact
from Yes_Bank.entity.config_entity import DataTransformationConfig
from Yes_Bank.components.data_transformation import DataTransformation

from Yes_Bank.entity.config_entity import ModelTrainerConfig
from Yes_Bank.components.model_train import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion_artifact= data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise YesBankException(e, sys)
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        try:
            data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(data_ingestion_artifact, data_transformation_config)
            data_transformation_artifact= data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:  
            raise YesBankException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            model_traner_config= ModelTrainerConfig(self.training_pipeline_config)
            model_trainer = ModelTrainer(model_traner_config, data_transformation_artifact)
            model_trainer_artifact= model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise YesBankException(e, sys)
        

    def run_pipeline(self):
        try:
            data_ingestion_artifact= self.start_data_ingestion()
            data_transformation_artifact= self.start_data_transformation(data_ingestion_artifact)
            model_trainer_artifact= self.start_model_trainer(data_transformation_artifact)
            return model_trainer_artifact
            
        
        except Exception as e:
            raise YesBankException(e, sys)
'''
this pipeline class can be called from app.py to strat the pipeline and run all the components sequentially and for prediction
purpose making the frontend of the project easy and simple.
'''