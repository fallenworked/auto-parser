# 🚗 Multi-Threaded Auto Classifieds Scraper (av.by / Drom / Auto.ru)

Высокопроизводительный парсер автомобильных объявлений с обходом блокировок Cloudflare / Akamai и поддержкой TLS Fingerprinting.

## ⚡ Особенности и Стек:
- **Python 3.10+**
- **curl_cffi** — подмена TLS-отпечатков браузера (Chrome 120/Firefox) без использования ресурсоемкого Selenium/Playwright.
- **BeautifulSoup4 & LXML** — быстрая обработка HTML-дерева.
- **Pandas / OpenPyXL** — автоматический экспорт результатов в XLSX / CSV.
- **Proxy Rotation Support** — поддержка мобильных и резидентных HTTP/SOCKS5 прокси.

## 🛠️ Установка и запуск

1. Клонировать репозиторий:
```bash
git clone [https://github.com/fallenworked/auto-parser.git](https://github.com/fallenworked/auto-parser.git)
cd auto-parser
