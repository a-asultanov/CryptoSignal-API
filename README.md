# CryptoSignal API
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
## License
MIT License © 2025 Arsen Asultanov
