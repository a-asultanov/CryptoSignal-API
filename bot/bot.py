import asyncio
import aiohttp
from time import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.config import BOT_TOKEN
from bot.utils import fetch_prices

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Получить цены")]],
        resize_keyboard=True
    )
    await message.answer(
        "Добро пожаловать в *CryptoSignal Bot*!\nНажмите кнопку чтобы получить текущие цены 👇",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

last_used = {}

@dp.message(lambda m: m.text == "Получить цены")
async def handle_get_prices(message: types.Message):
    now = time()
    user_id = message.from_user.id

    if user_id in last_used and now - last_used[user_id] < 5:
        await message.answer("Пожалуйста подождите...")
        return
    last_used[user_id] = now


    await message.answer("Получаем текущие цены...")

    session = aiohttp.ClientSession()
    try:
        await session.post("http://127.0.0.1:5000/api/coins/update")

        async with session.get("http://127.0.0.1:5000/api/coins") as response:
            coins = await response.json()
    finally:
        await session.close()

    if not coins:
        await message.answer("Информация недоступна")
        return

    text = "\n".join([f"{c['symbol']}: ${c['price']}" for c in coins])
    await message.answer(f"Current prices:\n{text}")

async def main():
    await dp.start_polling(bot, handle_signals=False)

if __name__ == "__main__":
    asyncio.run(main())