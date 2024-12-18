# -- Import Modules --
from random import choice
from pandas import DataFrame, concat
import os

# Config
from src.config import Config
config = Config()

# Scrapper
from modules.scrapper import Scrapper
scrapper = Scrapper(
    url = config.vars.URL,
    agent = choice(config.user_agents),
    pages = 5
)

# Extract htmls
soups = scrapper.get_soups()
print(f'\nForam extraídas {len(soups)} páginas.')
print(f"Amostra de Soup: {soups[0]}\n\n")

# Extract data
data_dicts = [scrapper.scrapping(soup) for soup in soups]
print(f"Foram extraídos {len(data_dicts)} registros.")
print(f"Amostra de Dados: {data_dicts[0]}\n\n")

dataframe = concat([DataFrame(data) for data in data_dicts], ignore_index = True)
print(f"Amostra de DataFrame: {dataframe.head()}\n\n")

# Creating data directory
data_path = os.path.join(config.project_dir, config.vars.data_dir)
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Saving data
dataframe.to_csv(
    os.path.join(config.project_dir, config.vars.data_dir, 'data.csv'),
    index = False
)