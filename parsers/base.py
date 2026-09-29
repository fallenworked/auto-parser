from abc import ABC, abstractmethod
from typing import List, Dict, Any
from curl_cffi import requests

class BaseParser(ABC):
    def __init__(self, proxy: str = None):
        self.proxy = proxy
        # Импрессия TLS-отпечатка Chrome 120 для обхода защиты
        self.session = requests.Session(impersonate="chrome120")
        if self.proxy:
            self.session.proxies = {"http": self.proxy, "https": self.proxy}

    @abstractmethod
    def fetch_page(self, page: int = 1) -> str:
        """Скачивает HTML-код страницы"""
        pass

    @abstractmethod
    def parse_cards(self, html: str) -> List[Dict[str, Any]]:
        """Извлекает данные из элементов страницы"""
        pass
