import logging
from curl_cffi import requests

def send_telegram_notification(token: str, chat_id: str, message: str) -> bool:
    """Отправка уведомления или отчета в Telegram канал/чат"""
    if not token or not chat_id:
        logging.info("ℹ️ Токен Telegram или Chat ID не указан. Уведомление пропущено.")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            logging.info("✅ Уведомление отправлено в Telegram")
            return True
        else:
            logging.error(f"❌ Не удалось отправить в Telegram: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"❌ Ошибка при отправке в Telegram: {e}")
        
    return False
