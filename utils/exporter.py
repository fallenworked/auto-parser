import pandas as pd
import json
import logging
from typing import List, Dict

def save_to_excel(data: List[Dict], filename: str = "auto_listings.xlsx") -> bool:
    """Сохранение списка словарей в Excel файл"""
    try:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        logging.info(f"✅ Данные сохранены в Excel: {filename} (всего {len(data)} записей)")
        return True
    except Exception as e:
        logging.error(f"❌ Ошибка при сохранении в Excel: {e}")
        return False

def save_to_json(data: List[Dict], filename: str = "auto_listings.json") -> bool:
    """Сохранение списка словарей в JSON файл"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"✅ Данные сохранены в JSON: {filename} (всего {len(data)} записей)")
        return True
    except Exception as e:
        logging.error(f"❌ Ошибка при сохранении в JSON: {e}")
        return False
