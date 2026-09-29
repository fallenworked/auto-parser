# 🚗 Multi-Threaded Auto Classifieds Scraper (av.by / Drom / Auto.ru)

Высокопроизводительный парсер автомобильных объявлений с обходом блокировок Cloudflare / Akamai и поддержкой TLS Fingerprinting.

## ⚡ Особенности и Стек
- **Python 3.10+**
- **curl_cffi** — подмена TLS-отпечатков браузера (Chrome 120/Firefox) без использования ресурсоемкого Selenium/Playwright.
- **BeautifulSoup4 & LXML** — быстрая обработка HTML-дерева.
- **Pandas / OpenPyXL** — автоматический экспорт результатов в XLSX / CSV.
- **Proxy Rotation Support** — поддержка мобильных и резидентных HTTP/SOCKS5 прокси.

## 📁 Структура проекта
```text
auto-parser/
├── config.py          # Настройки (прокси, заголовки, лимиты)
├── main.py            # Главный скрипт запуска
├── parsers/           # Модули парсеров
│   ├── __init__.py
│   ├── base.py
│   └── av_by.py
├── utils/             # Вспомогательные функции (экспорт, уведомления)
│   ├── __init__.py
│   ├── exporter.py
│   └── notifier.py
├── requirements.txt
└── README.md
```

## 🛠️ Установка и запуск

1. Клонировать репозиторий:
```bash
git clone [https://github.com/fallenworked/auto-parser.git](https://github.com/fallenworked/auto-parser.git)
cd auto-parser
```

2. Установить зависимости:
```bash
pip install -r requirements.txt
```

3. Запустить парсер:
```bash
python main.py
```

## 👨‍💻 Автор и контакты
- **Автор**: fallenworked
- **GitHub**: [fallenworked](https://github.com/fallenworked)
- **Telegram**: [@caxaold](https://t.me/caxaold)
