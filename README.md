# CryptoSignal API 
CryptoSignal API — это минималистичное серверное приложение на Flask с базой данных SQLite, предназначенное для отслеживания курсов криптовалют через CoinGecko API.  
Проект также включает Telegram-бота на Aiogram 3, который позволяет пользователям получать актуальные цены прямо в чате.

## Возможности
- REST API для получения и обновления цен  
- Асинхронное получение данных с CoinGecko  
- Telegram-бот для просмотра курсов  
- Простая архитектура без лишнего кода  
- Совместный запуск Flask-сервера и бота

## Используемые технологии
Flask, SQLAlchemy, Aiogram 3, aiohttp, asyncio, SQLite

## Установка
1. Клонировать репозиторий и создать виртуальное окружение:
   ```bash
   git clone https://github.com/a-asultanov/CryptoSignal-API.git
   cd CryptoSignal-API
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Настроить файл `.env`:
   ```
   FLASK_ENV=development
   SECRET_KEY=dev-flask-secret
   JWT_SECRET_KEY=dev-jwt-secret
   DATABASE_URL=sqlite:///crypto.db
   BOT_TOKEN=токен_вашего_бота
   PRICE_API_URL=https://api.coingecko.com/api/v3/simple/price
   UPDATE_INTERVAL=300
   ```
3. Инициализировать базу данных:
   ```bash
   python init_db.py
   python seed_coins.py
   ```
4. Запустить API и бота:
   ```bash
   python -m main
   ```

## Точки доступа API
`GET /api/status` — проверка состояния API  
`GET /api/coins` — список монет и их цены  
`POST /api/coins/update` — обновление цен через CoinGecko  

---

Примечание: Поддержка JWT-авторизации запланирована в следующих версиях.

---

## English
CryptoSignal API is a minimal backend service built with Flask and SQLAlchemy that tracks cryptocurrency prices via the CoinGecko API. It also includes a Telegram bot built with Aiogram 3 that allows users to request live prices directly from chat.
## Features
- RESTful Flask API with SQLite database  
- Real-time price fetching using CoinGecko  
- Telegram bot integration with Aiogram 3  
- Simple architecture and combined Flask + bot runtime  
## Stack
Flask, SQLAlchemy, Aiogram 3, aiohttp, asyncio, SQLite
## Setup
1. Clone the repo and create a virtual environment:
   ```bash
   git clone https://github.com/a-asultanov/CryptoSignal-API.git
   cd CryptoSignal-API
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Create a `.env` file:
   ```
   FLASK_ENV=development
   SECRET_KEY=dev-flask-secret
   JWT_SECRET_KEY=dev-jwt-secret
   DATABASE_URL=sqlite:///crypto.db
   BOT_TOKEN=your_telegram_bot_token_here
   PRICE_API_URL=https://api.coingecko.com/api/v3/simple/price
   UPDATE_INTERVAL=300
   ```
3. Initialize and seed the database:
   ```bash
   python init_db.py
   python seed_coins.py
   ```
4. Run both API and bot:
   ```bash
   python -m main
   ```
## Endpoints
`GET /api/status` — check API health  
`GET /api/coins` — list coins and prices  
`POST /api/coins/update` — refresh prices from API  

---

Note: Authentication (JWT) is planned for a future version.

