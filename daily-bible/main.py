from datetime import date
from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from scraper import WebScraper
from discord.ext import commands
import discord
import os


user_day = DayCounter()
user_verse = VerseFetcher()
scraper = WebScraper()


#Call add_day method when current date is changed
current_date = str(date.today())
origin_date = user_day.origin_date

if current_date != origin_date:
    origin_date = current_date
    user_day.add_day()


def scrape_verse():
    """
    Provide a list of dictionaries containing the reference & verses for the day.
    """
    current_verse = user_verse.daily_verse(user_day.day)

    #Consider saving the scraped verses into a variable which can be accessed later. Create a list of dictionaries where book-chapter is the key and the passage is the value.
    current_day_output = []

    scraper.open_site()

    #Loop through all items in list
    current_day_output = [{'reference': verse, 'verse': scraper.scrape_verse(verse)} for verse in current_verse]

    scraper.quit()

    return current_day_output

def send_verse(send_verse_list):
    """
    Format the verses to be readable.
    """
    for message in send_verse_list:
        print(f"{message['reference']}\n")
        print(f"{message['verse']}\n")
        print("--------------------------------- \n")

send_verse(scrape_verse())

# #Discord Bot Settings
# TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
# CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# @bot.event
# async def on_ready():
#     print("Hello!")
#     channel = bot.get_channel(CHANNEL_ID)
#     await channel.send("Hello, I'm ready to roll out!")

# #Commands Samples
# #For each command, you need to add the line @bot.command()

# @bot.command()
# #Say Hello
# async def hello(ctx):
#     await ctx.send("Hello!")

# #Add integers
# @bot.command()
# async def add(ctx, x, y):
#     sum = int(x) + int(y)
#     await ctx.send(f'{sum}')

# bot.run(TOKEN)
