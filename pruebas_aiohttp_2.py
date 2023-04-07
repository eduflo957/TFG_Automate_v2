import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://es.lyricstraining.com/') as response:

            print("XXXX-Status:", response.status)
            print("XXXX-Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:20], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())