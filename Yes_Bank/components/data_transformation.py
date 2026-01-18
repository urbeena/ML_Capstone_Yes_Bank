import sys
import pandas as pd
import numpy as np

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
from Yes_Bank.entity.config_entity import DataTransformationConfig
from Yes_Bank.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
)

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from Yes_Bank.utils.main_utils.utils import save_object, save_numpy_array_data


class DataTransformation:
    
    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_transformation_config: DataTransformationConfig,
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise YesBankException(e, sys)

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
            logger.logging.info(f"Read data from {file_path} successfully")
            return df
        except Exception as e:
            raise YesBankException(e, sys)

    @staticmethod
    def convert_date_column(df: pd.DataFrame) -> pd.DataFrame:
        """
        Converts Date column like 'Dec-10' into numeric Month & Year
        """
        try:
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"], format="%b-%y")
                df["Month"] = df["Date"].dt.month
                df["Year"] = df["Date"].dt.year
                df.drop(columns=["Date"], inplace=True)

                logger.logging.info(f"Converted Date column to Month and Year{df['Year'].unique().tolist()}")

            return df

        except Exception as e:
            raise YesBankException(e, sys)

    def data_transformer_object(self) -> Pipeline:
        try:
            imputer = SimpleImputer(strategy="median")
            processor = Pipeline(
                steps=[
                    ("imputer", imputer),
                ]
            )
            return processor
        except Exception as e:
            raise YesBankException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            train_df = self.read_data(self.data_ingestion_artifact.train_path)
            test_df = self.read_data(self.data_ingestion_artifact.test_path)

            logger.logging.info(
                "Read train and test data successfully for transformation"
            )

            # Convert Date column
            train_df = self.convert_date_column(train_df)
            test_df = self.convert_date_column(test_df)

            target_column = "Close"

            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]

            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            logger.logging.info(
                f"Input features: {X_train.columns.tolist()}, Target: {target_column}"
            )

            processor = self.data_transformer_object()

            X_train_transformed = processor.fit_transform(X_train)
            X_test_transformed = processor.transform(X_test)

            train_arr = np.c_[X_train_transformed, np.array(y_train)]
            test_arr = np.c_[X_test_transformed, np.array(y_test)]

            save_numpy_array_data(
                self.data_transformation_config.transformed_train_path,
                train_arr,
            )
            
            save_numpy_array_data(
                self.data_transformation_config.transformed_test_path,
                test_arr,
            )

            save_object(
                self.data_transformation_config.transformed_object_path,
                processor,
            )

            save_object( "final_model/preprocessor.pkl", 
                processor,
            )

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_path=self.data_transformation_config.transformed_train_path,
                transformed_test_path=self.data_transformation_config.transformed_test_path,
                preprocessor_object_path=self.data_transformation_config.transformed_object_path,
            )

            logger.logging.info("Data Transformation completed successfully")

            return data_transformation_artifact

        except Exception as e:
            raise YesBankException(e, sys)



