#Data ingestion = loading + collecting + storing raw data
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

@dataclass ##You write __init__ only when a class needs to store or initialize data. If the class just has methods, or uses @dataclass, you don’t need to write __init__
class DataIngestionConfig: ##This class does NOT create folders. It only stores paths.
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() ##basically object of the above class
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=pd.read_csv('notebook\data\student.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)##Create artifacts folder if it doesn’t exist
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) ##index=False means: Don’t save row numbers header=True means Keep column names
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

