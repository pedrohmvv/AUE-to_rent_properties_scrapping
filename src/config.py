# -- Import modules --
from dataclasses import dataclass
from yaml import load
from yaml.loader import SafeLoader
from os.path import join, dirname, abspath

@dataclass
class Variables:
    URL: str
    section_class: str
    data_dir: str
    article: str
    details_class: str
    price_class: str
    id_price: str
    location_class: str
    id_bedrooms_class: str
    id_bathroom_class: str
    id_area_class: str
    button_div: str
    link_id: str
    call_id: str
    id_time: str

class Config:
    """Basic Config class"""

    def __init__(self):
        """Initialize instance"""
        self.project_dir = dirname(abspath(__file__))
        data = {}
        with open(
            join(dirname(abspath(__file__)), 'vars.yaml'), encoding = 'utf-8'
        ) as file:
            data = load(file, Loader=SafeLoader)
        self.vars = Variables(
            URL = data.get('URL'),
            data_dir= data.get('data_dir'),
            section_class = data.get('section_class'),
            article = data.get('article'),
            details_class = data.get('details_class'),
            price_class = data.get('price_class'),
            id_price = data.get('id_price'),
            location_class = data.get('location_class'),
            id_bedrooms_class = data.get('id_bedrooms_class'),
            id_bathroom_class = data.get('id_bathroom_class'),
            id_area_class = data.get('id_area_class'),
            button_div = data.get('button_div'),
            link_id= data.get('link_id'),
            call_id = data.get('call_id'),
            id_time= data.get('id_time')
        )
        self.user_agents = [
            'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        ]