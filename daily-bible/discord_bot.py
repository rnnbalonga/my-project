from discord.ext import commands
import discord
import os

class DiscordBot:
    TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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

        
    bot.run(TOKEN)
