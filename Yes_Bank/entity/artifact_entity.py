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

