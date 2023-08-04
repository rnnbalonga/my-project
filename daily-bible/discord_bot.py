from discord.ext import commands
import discord

TOKEN = "MTEzNjgyNDk5NzcxNzk5OTYzNg.GO44FB.kWeBLVZR0PX_Ow3IT9s7PW5UA2cWp4r7G25_u0"
CHANNEL_ID = 1136829338206077028

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello, I'm ready to roll out!")

bot.run(TOKEN)
