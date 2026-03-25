import os
import asyncio
import datetime
import discord as dihcord #Alias discord as "dihcord" hehe
import orjson
from dotenv import load_dotenv

load_dotenv() #Allows loading of environment variables

loop = asyncio.new_event_loop() #Creates async event loop because py-cord no longer packages this by default
asyncio.set_event_loop(loop)

intents = dihcord.Intents.default() #Sets required intents for the bot
bot = dihcord.Bot(intents=intents) #Creates discord bot object


# Persistent storage
def save():
    save_data = {
        "time": datetime.datetime.now(),
        "puzzle_is_enabled": puzzle_is_enabled,
        "leaderboard": leaderboard
    }
    with open("clutch_data.json", "wb") as f:
        f.write(orjson.dumps(save_data, option=orjson.OPT_INDENT_2))
def load():
    global puzzle_is_enabled
    global leaderboard
    with open("clutch_data.json", "rb") as f:
        load_data: dict = orjson.loads(f.read())
    puzzle_is_enabled = load_data["puzzle_is_enabled"]
    leaderboard = load_data["leaderboard"]



# Puzzle feature
#Should be set to the CHANNEL_ID of the daily and weekly puzzles channel
channel = bot.get_channel(00000000)
puzzle_is_enabled: bool = False
#Leaderboard of points and solved puzzles
leaderboard: list[tuple[int, int]] #List of (user id, score)
#Loads daily and weekly puzzles into memory
with open("puzzles.json", "rb") as f:
    puzzle_data: dict = orjson.loads(f.read())
#The view class for the weekly puzzle
class WeeklyPuzzleView(dihcord.ui.View):
    #Embed for the weekly puzzle
    puzzle_embed = dihcord.Embed(
        title=f"Weekly puzzle #{puzzle_data["puzzle_count"]}",
        author=dihcord.EmbedAuthor(name="nniro", url="https://github.com/reallynniroprobably"),
        fields=[
            dihcord.EmbedField(name="Puzzle", value=puzzle_data["weekly_puzzle"], inline=False)
        ],
        footer=dihcord.EmbedFooter(text="We kindly ask that you do NOT use artificial intelligence for the challenges.")
    )
    @dihcord.ui.button(label="Input")
    async def puzzle_button(self, button, interaction: dihcord.Interaction): #Remember to add the link for the input here
        return
@bot.slash_command(name="toggle_puzzle") #Administrator command to toggle weekly and daily puzzles
@dihcord.default_permissions(administrator=True)
async def toggle_puzzle(ctx):
    global puzzle_is_enabled
    if puzzle_is_enabled:
        puzzle_is_enabled = False
        ctx.respond("Puzzles have been disabled", ephemeral=True)
    else:
        puzzle_is_enabled = True
        ctx.respond("Puzzles have been enabled", ephemeral=True)
    save()


load()



bot.run(os.getenv("DISCORD_TOKEN"))