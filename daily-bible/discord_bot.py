from discord.ext import commands
import discord
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#cogs

def sample():
    print("This is a sample")

@bot.event
async def on_ready():
    print("Hello!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello, I'm ready to roll out!")

#Commands Samples
#For each command, you need to add the line @bot.command()

@bot.command()
#Say Hello
async def hello(ctx):
    await ctx.send("Hello!")

#Add integers
@bot.command()
async def add(ctx, x, y):
    sum = int(x) + int(y)
    await ctx.send(f'{sum}')

#Figure out a way to take a function as an input and execute that function with a keyword

#List of commands
#!today = give today's verse via main()
#!setday = allows user to set the day of passage they want to read. 
#
    
bot.run(TOKEN)
