from src.modules.scrapper import Scrapper
from src.config import Config

from random import choice
from pandas import DataFrame, concat

import os
import logging

class Extract:
    """Excract data interface"""
    def __init__(self, pages: int = 100, **airflow_context: dict) -> None:
        """Initialize instance"""
        self.airflow_context = airflow_context
        self.config = Config()
        # Data Dir
        self.data_dir = os.path.join(self.config.project_dir, self.config.vars.data_dir)
        self.file_path = os.path.join(self.data_dir, 'data.csv')
        os.makedirs(self.data_dir, exist_ok =True)
        # Scrapper
        self.scrapper = Scrapper(
            url = self.config.vars.URL,
            agent = choice(self.config.user_agents),
            pages = pages
        )
        
    def check_processed_data(self):
        pass

    def __extract(self) -> DataFrame:
        soups = self.scrapper.get_soups()
        data_dicts = [self.scrapper.scrapping(soup) for soup in soups]
        dataframe = concat([DataFrame(data) for data in data_dicts], ignore_index = True)
        return dataframe
    
    def execute(self) -> bool:
        """Execute extract"""
        try:
            dataframe = self.__extract()
            dataframe.to_csv(self.file_path, index = False)
            logging.info(f"Data extracted and saved to {self.file_path}")
            return True
        except Exception as e:
            logging.error(f"Error: {e}")
            return False