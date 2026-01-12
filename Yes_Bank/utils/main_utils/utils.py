from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
import sys
import os
import numpy as np
import pandas as pd
import pickle

def save_numpy_array_data(file_path: str,array:np.array):
    '''
    save numpy array data to file
    '''
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
     raise YesBankException(e,sys)
    
def load_numpy_array_data(file_path: str)->np.array:
    '''
    load numpy array data from file
    '''
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
     raise YesBankException(e,sys)
    
def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise YesBankException(e, sys)
    
def save_object(file_path: str, obj: object) -> None:
    try:
        logger.logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logger.logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise YesBankException(e, sys)