import logging
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from parsers.base import BaseParser

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AvByParser(BaseParser):
    def fetch_page(self, page: int = 1) -> str:
        url = f"https://cars.av.by/filter?page={page}"
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "referer": "https://av.by/",
        }
        
        logging.info(f"Запрос страницы {page}...")
        try:
            response = self.session.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                return response.text
            logging.error(f"Ошибка запроса: Статус {response.status_code}")
        except Exception as e:
            logging.error(f"Сбой при запросе страницы {page}: {e}")
        return ""

    def parse_cards(self, html: str) -> List[Dict[str, Any]]:
        if not html:
            return []

        soup = BeautifulSoup(html, "lxml")
        cards = soup.find_all("div", class_="listing-item")
        results = []

        for card in cards:
            try:
                title_elem = card.find("a", class_="listing-item__link")
                price_elem = card.find("div", class_="listing-item__price")
                usd_price_elem = card.find("div", class_="listing-item__price-usd")
                params_elem = card.find("div", class_="listing-item__params")
                
                if not title_elem:
                    continue

                title = title_elem.text.strip()
                link = "https://cars.av.by" + title_elem.get("href", "")
                price = price_elem.text.strip() if price_elem else "N/A"
                price_usd = usd_price_elem.text.strip() if usd_price_elem else "N/A"
                params = params_elem.text.strip().replace("\n", " ") if params_elem else ""

                results.append({
                    "title": title,
                    "price_byn": price,
                    "price_usd": price_usd,
                    "params": params,
                    "link": link
                })
            except Exception as e:
                logging.warning(f"Ошибка при разборе карточки: {e}")

        return results
