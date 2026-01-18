from Yes_Bank.constant.training_pipeline import MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_FILE_NAME
import os
import sys
from Yes_Bank.logging.logger import logging
from Yes_Bank.exception.exception import YesBankException

class YesBankModel:
    def __init__(self,preprocessor,model):
        self.preprocessor= preprocessor
        self.model= model
    def predict(self, X):
        try:
            X_transformed= self.preprocessor.transform(X)
            preds= self.model.predict(X_transformed)
            return preds
        except Exception as e:
            raise YesBankException(e, sys)