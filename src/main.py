import os
import asyncio
import discord as dihcord
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
intents = dihcord.Intents.default()
bot = dihcord.Bot(intents=intents)


# Commands









bot.run(os.getenv("DISCORD_TOKEN"))