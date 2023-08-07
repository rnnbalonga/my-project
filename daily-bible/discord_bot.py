from discord.ext import commands
import discord
import os


class DiscordBot:
    def __init__(self):
        self.TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
        self.CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
        self.bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
        self.bot.run(self.TOKEN)

    @bot.event
    async def on_ready(self):
        print("Hello!")
        channel = self.bot.get_channel(self.CHANNEL_ID)
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

    
