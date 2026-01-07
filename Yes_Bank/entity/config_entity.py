from Yes_Bank.constant import training_pipeline
import os

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = training_pipeline.ARTIFACT_DIR


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.raw_data_path = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
            training_pipeline.RAW_DATA_PATH
        )
        
        self.train_data_path = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
            training_pipeline.TRAINING_PATH
        )

        self.test_data_path = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
            training_pipeline.TESTING_PATH
        )
        