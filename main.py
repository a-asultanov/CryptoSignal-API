import threading
import asyncio
import time
from app import create_app
from bot.bot import main as run_bot

def run_flask():
    app = create_app()
    app.run(debug=True, use_reloader=False)

def run_telegram_bot():
    asyncio.run(run_bot())

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)

    flask_thread.start()
    bot_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Flask and Telegram Bot...")