import os
import sys
from typing import Dict

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
from sklearn.model_selection import GridSearchCV

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging.logger import logging
from Yes_Bank.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ClassificationMetricArtifact
)
from Yes_Bank.entity.config_entity import ModelTrainerConfig
from Yes_Bank.utils.main_utils.utils import (
    load_numpy_array_data,
    save_object,
    load_object
)

from Yes_Bank.utils.ml_utils.estimator import YesBankModel

class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        data_transformation_artifact: DataTransformationArtifact
    ):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise YesBankException(e, sys)

    # ---------------------------------------------------------
    # Train & evaluate all models
    # ---------------------------------------------------------
    def train_model(self, X_train, y_train, X_test, y_test) -> ModelTrainerArtifact:
        try:
            models: Dict[str, object] = {
                "LinearRegression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "DecisionTreeRegressor": DecisionTreeRegressor(),
                "RandomForestRegressor": RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "AdaBoostRegressor": AdaBoostRegressor()
            }

            params = {
                "LinearRegression": {},
                "Ridge": {"alpha": [0.1, 1.0, 10.0, 100.0]},
                "Lasso": {"alpha": [0.1, 1.0, 10.0, 100.0]},
                "KNeighborsRegressor": {"n_neighbors": [3, 5, 7, 9]},
                "DecisionTreeRegressor": {"max_depth": [5, 10, 15]},
                "RandomForestRegressor": {
                    "n_estimators": [50, 100, 200],
                    "max_depth": [5, 10]
                },
                "GradientBoostingRegressor": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2]
                },
                "AdaBoostRegressor": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 0.2]
                }
            }

            model_report = {}

            logging.info("Starting model training & evaluation")

            for model_name, model in models.items():
                logging.info(f"Training model: {model_name}")

                gs = GridSearchCV(
                    estimator=model,
                    param_grid=params[model_name],
                    cv=5,
                    n_jobs=-1
                )
                gs.fit(X_train, y_train)

                best_model = gs.best_estimator_
                best_model.fit(X_train, y_train)

                y_train_pred = best_model.predict(X_train)
                y_test_pred = best_model.predict(X_test)

                model_report[model_name] = {
                    "model": best_model,
                    "train_r2": r2_score(y_train, y_train_pred),
                    "test_r2": r2_score(y_test, y_test_pred)
                }

            # ---------------------------------------------------------
            # Select best model
            # ---------------------------------------------------------
            best_model_name = max(
                model_report,
                key=lambda name: model_report[name]["test_r2"]
            )

            best_model = model_report[best_model_name]["model"]
            best_test_r2 = model_report[best_model_name]["test_r2"]

            logging.info(
                f"Best model selected: {best_model_name} "
                f"with test R2: {best_test_r2}"
            )

            # ---------------------------------------------------------
            # Metrics Artifact
            # ---------------------------------------------------------
            y_test_pred = best_model.predict(X_test)

            test_metric_artifact = ClassificationMetricArtifact(
                model_name=best_model_name,
                model_mse=mean_squared_error(y_test, y_test_pred),
                model_mae=mean_absolute_error(y_test, y_test_pred),
                model_r2=r2_score(y_test, y_test_pred)
            )

            # ---------------------------------------------------------
            # Save model
            # ---------------------------------------------------------

            preprocessor= load_object(
                self.data_transformation_artifact.preprocessor_object_path)
            
            
            YesBank_Model = YesBankModel(preprocessor=preprocessor, model=best_model)

            model_dir = os.path.dirname(
                self.model_trainer_config.trained_model_file_path
            )
            os.makedirs(model_dir, exist_ok=True)

            save_object(self.model_trainer_config.trained_model_file_path,obj=YesBank_Model)

          

            save_object("final_model/model.pkl", best_model)
            

            logging.info("Best trained model saved successfully")

            return ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric_artifact=None,
                test_metric_artifact=test_metric_artifact
            )

        except Exception as e:
            raise YesBankException(e, sys)

    # ---------------------------------------------------------
    # Pipeline entry point
    # ---------------------------------------------------------
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_arr = load_numpy_array_data(
                self.data_transformation_artifact.transformed_train_path
            )
            test_arr = load_numpy_array_data(
                self.data_transformation_artifact.transformed_test_path
            )

            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            return self.train_model(X_train, y_train, X_test, y_test)

        except Exception as e:
            raise YesBankException(e, sys)
