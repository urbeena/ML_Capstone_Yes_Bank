from dataclasses import dataclass
from Yes_Bank.logging import logger
@dataclass
class DataIngestionArtifact:
    train_path: str
    test_path: str

    def __post_init__(self):
        logger.logging.info(f"train_path={self.train_path}, test_path={self.test_path}"
        )
    


@dataclass
class DataTransformationArtifact:
    transformed_train_path: str
    transformed_test_path: str
    preprocessor_object_path: str

@dataclass
class ClassificationMetricArtifact:
    model_name: str
    model_mse: float
    model_mae: float
    model_r2: float


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact