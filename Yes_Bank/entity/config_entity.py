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
        )#artifact/data_ingestion/rawdata.csv
        
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

class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.transformed_train_path=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.DATA_TRANSFORMATION_TRAIN_FILE_PATH
        )
        self.transformed_test_path=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.DATA_TRANSFORMATION_TEST_FILE_PATH
        )
        self.transformed_object_path=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
             training_pipeline.preprocessor_obj)
        
class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir= os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path= os.path.join(
            self.model_trainer_dir,
            training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
            training_pipeline.MODEL_FILE_NAME
        )

        self.expected_score= training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold= training_pipeline.MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD


