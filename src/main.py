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

#Command to ping people when the specified people are online
ping_map = defaultdict(list)
@bot.slash_command(name="online_ping", description="Pings you when the selected user is online", guild_ids=[1483649833922203691])
async def online_ping(ctx, user: dihcord.Option(dihcord.User, "The user to be pinged for")): #noqa
    await ctx.respond(f"Successfully added {user.name} to your watchlist!", ephemeral=True)
    ping_map[user].append(ctx.author)
    print(f"{ctx.author} added {user} to their watchlist!")
@bot.listen("on_message")
async def ping_user(message: dihcord.Message):
    if message.author == bot.user:
        return
    if message.author in ping_map:
        for user in ping_map[message.author]:
            await user.send(f"Hey! {message.author.name} is online!")
            print(f"{user} was pinged when {message.author} talked!")








bot.run(os.getenv("DISCORD_TOKEN"))