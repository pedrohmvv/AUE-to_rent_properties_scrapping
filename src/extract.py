from modules.scrapper import Scrapper
from config import Config

from random import choice
from pandas import DataFrame, concat

import os

class Extract:
    """Excract data interface"""
    def __init__(self, pages: int = 100, **airflow_context: dict) -> None:
        """Initialize instance"""
        self.airflow_context = airflow_context
        self.config = Config()
        self.scrapper = Scrapper(
            url = self.config.vars.URL,
            agent = choice(self.config.user_agents),
            pages = pages
        )
        
    def check_processed_data(self):
        pass

    def execute(self) -> DataFrame:
        soups = self.scrapper.get_soups()
        data_dicts = [self.scrapper.scrapping(soup) for soup in soups]
        dataframe = concat([DataFrame(data) for data in data_dicts], ignore_index = True)
        return dataframe
