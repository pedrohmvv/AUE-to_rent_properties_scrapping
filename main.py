# -- Import Modules --
from random import choice
from pandas import DataFrame, concat
import os

# Config
from src.config import Config
config = Config()

# Scrapper
from src.modules.scrapper import Scrapper
scrapper = Scrapper(
    url = config.vars.URL,
    agent = choice(config.user_agents),
    pages = 5
)

# Extract
from src.extract import Extract
extract = Extract(pages = 5)

# Extract data
data = extract.execute()