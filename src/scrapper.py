# -- Import Modules --
from requests import get
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# -- Import Config --
from src.config import Config
config = Config()

class Scrapper:
    """Classe para extrair dados de um site de anúncios de imóveis"""
    def __init__(self, url: str, agent: str, pages: int = 100):
        self.url = url
        self.agent = agent
        self.pages = pages
        self.config = Config()

    def get_soups(self) -> object:
        """
        Extrai os htmls de todas as páginas
        -----------------------------------
        Return:
            soup (BeautifulSoup): Objeto BeautifulSoup
        """
        page = 0
        sufix = lambda page: f'?page={page}' if page > 0 else ''
        soups = []
        
        while page < self.pages:
            try:
                url = ''.join([self.url, sufix(page)])
                response = get(url=url, headers={'User-agent': self.agent})
                response.raise_for_status()
                print(f'\rExtraindo página {page}', end='')
                soup = BeautifulSoup(response.text, 'html.parser')
                soups.append(soup)
                page += 1
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}. Página {page} não encontrada.')
                return soups
        return soups
    
    def extract_text(self, element: object,  default: str = "") -> str:
        """
        Extrai o texto de um elemento
        -----------------------------
        Args:
            element (object): Objeto BeautifulSoup
            selector (string): Seletor CSS
        Return:
            string: Texto extraído
        """
        try:
            if isinstance(element, list):
                return element[-1].get_text(strip=True)
            return element.get_text(strip=True)
        except (AttributeError, IndexError, TypeError) as e:
            print(f"Erro ao extrair texto: {e}")
            return default
        
    def parse_article(self, article: BeautifulSoup) -> dict:
        try:
            session = article.find('section', {"class": self.config.vars.section_class})
            return {
                "Details": [self.extract_text(session.find('h2', {'class': self.config.vars.details_class}))],
                "Price": [self.extract_text(session.find('p', {'data-testid': self.config.vars.id_price}))],
                "Location": [self.extract_text(session.find('p', {'class': self.config.vars.location_class}))],
                "Bedrooms": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_bedrooms_class}))],
                "Bathrooms": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_bathroom_class}))],
                "Area": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_area_class}))],
                "Link": [article.find('a', {'data-testid': 'property-card-link'})['href']],
                "Contact": [article.find('a', {'data-testid': self.config.vars.call_id})['href']]
            }
        except Exception as e:
            print(f"Erro ao extrair dados do artigo: {e}")
            return {}
    
    def scrapping(self, soup: object = None) -> dict:
        """
        Extrai os dados do site
        -----------------------
        Args:
            soup (BeautifulSoup): Objeto BeautifulSoup
        Return:
            dict: Dicionário com os dados extraídos
        """
        if soup is None:
            return {}
        
        # Dicionário para armazenar os dados extraídos
        data = {
            "Details": [],
            "Price": [],
            "Location": [],
            "Bedrooms": [],
            "Bathrooms": [],
            "Area": [],
            "Link": [],
            "Contact": []
        }

        # Get properties cards
        articles = soup.find_all('article', {"data-testid": self.config.vars.article})
        for article in articles:
            data.update(self.parse_article(article))

        return data