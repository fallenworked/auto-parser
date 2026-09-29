import logging
from config import PROXY, MAX_PAGES, TG_TOKEN, TG_CHAT_ID
from parsers import AvByParser
from utils import save_to_excel, save_to_json, send_telegram_notification

def main():
    logging.info("🚀 Запуск парсера авто-объявлений...")
    
    # Инициализация парсера
    parser = AvByParser(proxy=PROXY if PROXY else None)
    
    all_data = []
    
    for page in range(1, MAX_PAGES + 1):
        html = parser.fetch_page(page)
        cards = parser.parse_cards(html)
        logging.info(f"Собрано {len(cards)} объявлений со страницы {page}")
        all_data.extend(cards)

    if all_data:
        # 1. Сохранение результатов
        save_to_excel(all_data, "auto_listings.xlsx")
        save_to_json(all_data, "auto_listings.json")
        
        # 2. Отправка отчета в Telegram
        report = (
            f"<b>🚗 Отчет по парсингу авто:</b>\n"
            f"• Собрано объявлений: <b>{len(all_data)}</b>\n"
            f"• Обработано страниц: <b>{MAX_PAGES}</b>\n"
            f"• Первое авто в списке: <i>{all_data[0]['title']}</i> ({all_data[0]['price_usd']})"
        )
        send_telegram_notification(TG_TOKEN, TG_CHAT_ID, report)
    else:
        logging.warning("⚠️ Не удалось собрать данные.")

if __name__ == "__main__":
    main()
