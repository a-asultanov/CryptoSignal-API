import aiohttp

async def fetch_prices():
    url = "http://127.0.0.1:5000/api/coins"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return []   