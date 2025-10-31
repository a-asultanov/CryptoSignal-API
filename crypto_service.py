import aiohttp
import asyncio
from config import Config

async def fetch_prices(symbols: list[str]) -> dict:
    url = Config.PRICE_API_URL
    params = {
        "ids": ",".join(symbols),
        "vs_currencies": "usd"
    }

    async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch data: {response.status}")
                data = await response.json()

    return {coin: info["usd"] for coin, info in data.items()}