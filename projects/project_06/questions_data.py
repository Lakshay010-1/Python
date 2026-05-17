import asyncio
import aiohttp

url = "https://opentdb.com/api.php?amount=50&difficulty=easy&type=boolean"

questions = []


async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def main():
    global questions
    result = await fetch_data()
    questions = result.get("results", [])


asyncio.run(main())
