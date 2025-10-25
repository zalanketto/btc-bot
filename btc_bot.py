import discord
import asyncio
import requests

TOKEN = "MTQzMDU4NTI1NzU1MTMzMTQ2OQ.GQm6-1.z2wXojrtdzAa61PkmskPuVZvuTfg_tOE5tOlco"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    data = requests.get(url).json()
    return data["bitcoin"]["usd"]

@client.event
async def on_ready():
    print(f"✅ Bejelentkezve mint {client.user}")
    while True:
        try:
            price = get_btc_price()
            print(f"BTC ár: ${price}")  # csak hogy lásd a konzolban
            activity = discord.Activity(
                type=discord.ActivityType.watching,
                name=f"BTC: ${price:,}"
            )
            await client.change_presence(activity=activity)
        except Exception as e:
            print(f"Hiba: {e}")
        await asyncio.sleep(60)  # frissítés 60 másodpercenként

import os
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)



