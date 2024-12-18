# -- Import Modules --
import logging
from requests import get
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# -- Import Config --
from src.config import Config
config = Config()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Scrapper:
    """Extract data from Property Finder website class"""
    
    def __init__(self, url: str, agent: str, pages: int = 100):
        """Initialize the scraper with URL, agent and number of pages to scrape"""
        self.url = url
        self.agent = agent
        self.pages = pages
        self.config = Config()

    def get_soups(self) -> list[BeautifulSoup]:
        """
        Extracts the HTML content from the website
        -----------------------------------------
        Return:
            soups (list): List of BeautifulSoup objects for each page
        """
        page = 0
        sufix = lambda page: f'?page={page}' if page > 0 else ''
        soups = []
        
        while page < self.pages:
            try:
                url = ''.join([self.url, sufix(page)])
                response = get(url=url, headers={'User-agent': self.agent})
                response.raise_for_status()
                logger.info(f'Extracting page {page}')
                soup = BeautifulSoup(response.text, 'html.parser')
                soups.append(soup)
                page += 1
                logger.info(f'Page {page} extracted successfully.')
            except HTTPError as http_err:
                logger.error(f'HTTP error occurred: {http_err}. Page {page} not found.')
                return soups
        return soups
    
    def extract_text(self, element: object, default: str = "") -> str:
        """
        Extracts the text from a given element
        --------------------------------------
        Args:
            element (object): BeautifulSoup object
            default (str): Default value to return in case of error
        Return:
            string: Extracted text or default value in case of error
        """
        try:
            if isinstance(element, list):
                return element[-1].get_text(strip=True)
            return element.get_text(strip=True)
        except (AttributeError, IndexError, TypeError) as e:
            logger.error(f"Error extracting text: {e}")
            return default
        
    def parse_article(self, article: BeautifulSoup) -> dict:
        """
        Parses a property article and extracts relevant data
        -----------------------------------------------------
        Args:
            article (BeautifulSoup): The article object to parse
        Return:
            dict: Extracted data from the article
        """
        try:
            session = article.find('section', {"class": self.config.vars.section_class})
            return {
                "Details": [self.extract_text(session.find('h2', {'class': self.config.vars.details_class}))],
                "Price": [self.extract_text(session.find('p', {'data-testid': self.config.vars.id_price}))],
                "Location": [self.extract_text(session.find('p', {'class': self.config.vars.location_class}))],
                "Bedrooms": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_bedrooms_class}))],
                "Bathrooms": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_bathroom_class}))],
                "Area": [self.extract_text(session.find_all('p', {'data-testid': self.config.vars.id_area_class}))],
                "Listing Time": [article.find('p', {'class': self.config.vars.id_time}).text],
                "Link": [article.find('a', {'data-testid': 'property-card-link'})['href']],
                "Contact": [article.find('a', {'data-testid': self.config.vars.call_id})['href']],
            }
        except Exception as e:
            logger.error(f"Error extracting data from article: {e}")
            return {}
    
    def scrapping(self, soup: object = None) -> dict:
        """
        Extracts data from the website
        -------------------------------
        Args:
            soup (BeautifulSoup): BeautifulSoup object containing the HTML content
        Return:
            dict: Dictionary with extracted data
        """
        if soup is None:
            return {}
        
        # Dictionary to store extracted data
        data = {
            "Details": [],
            "Price": [],
            "Location": [],
            "Bedrooms": [],
            "Bathrooms": [],
            "Area": [],
            "Link": [],
            "Contact": [],
            "Listing Time": []
        }

        # Get properties cards
        articles = soup.find_all('article', {"data-testid": self.config.vars.article})
        for article in articles:
            article_data = self.parse_article(article)
            if article_data:
                data.update(article_data)

        return data
