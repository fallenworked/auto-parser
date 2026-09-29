import os

# Прокси (поддерживаются HTTP / SOCKS5, например Asocks или Smartproxy)
PROXY = os.getenv("PROXY_URL", "http://user:password@proxy_host:port")

# Настройки поиска
MAX_PAGES = 3
TARGET_URL = "https://cars.av.by/filter"

# Telegram Bot (необязательно, для алертов)
TG_TOKEN = os.getenv("TG_TOKEN", "")
TG_CHAT_ID = os.getenv("TG_CHAT_ID", "")
