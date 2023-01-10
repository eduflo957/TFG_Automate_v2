import pandas as pd
import webbrowser
from urllib.request import urlopen
import asyncio

def main():
    url = "https://twitter.com/SoyHijoDelPerro"
    webbrowser.open(url, new=0, autoraise=True) 

    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            # print(await resp.text())


if __name__=='__main__':
    run(main())