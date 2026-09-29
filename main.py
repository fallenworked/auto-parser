import pandas as pd
import logging
from parsers.av_by import AvByParser
from config import PROXY, MAX_PAGES

def main():
    logging.info("🚀 Запуск парсера авто-объявлений...")
    parser = AvByParser(proxy=None) # Замените на PROXY, если используете прокси
    
    all_data = []
    
    for page in range(1, MAX_PAGES + 1):
        html = parser.fetch_page(page)
        cards = parser.parse_cards(html)
        logging.info(f"Собрано {len(cards)} объявлений со страницы {page}")
        all_data.extend(cards)

    if all_data:
        df = pd.DataFrame(all_data)
        output_file = "auto_listings.xlsx"
        df.to_excel(output_file, index=False)
        logging.info(f"✅ Готово! Результаты сохранены в {output_file} (Всего: {len(all_data)} записей)")
    else:
        logging.warning("⚠️ Не удалось собрать данные.")

if __name__ == "__main__":
    main()
