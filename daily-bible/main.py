from day_counter import DayCounter
from verse_fetcher import VerseFetcher
import datetime
import time
# from discord_bot import DiscordBot

user_day = DayCounter()
user_verse = VerseFetcher()

#Get user_verse list from user_day
current_verse = user_verse.daily_verse(user_day.day)
print(f"Current verse: {current_verse}")

#Call user_day.add_day() after 12AM
current_date = datetime.date.today()

while True:
    time.sleep(1)
    new_date = datetime.date.today()
    if new_date > current_date:
        user_day.add_day()
        current_date = new_date 

