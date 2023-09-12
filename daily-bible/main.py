from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from selenium.webdriver.common.by import By
import schedule
import time


# from discord_bot import DiscordBot

user_day = DayCounter()
user_verse = VerseFetcher()

#Get user_verse list from user_day
current_verse = user_verse.daily_verse(user_day.day)
print(f"Current verse: {current_verse}")

# #Call user_day.add_day() after 12AM
# schedule.every().day.at("00:00").do(user_day.add_day)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#Webscrape
