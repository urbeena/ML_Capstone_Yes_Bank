import pandas as pd
from Yes_Bank.logging import logger   
from Yes_Bank.exception.exception import YesBankException
import sys  
file_path = "data/data_YesBank_StockPrices.csv"

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully")
        return df
    except Exception as e:
        raise YesBankException(e, sys)


logger.logging.info("Data loaded successfully")