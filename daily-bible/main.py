from day_counter import DayCounter
from verse_fetcher import VerseFetcher
# from discord_bot import DiscordBot

user_day = DayCounter()
user_verse = VerseFetcher()
# bot = DiscordBot()

print(user_day.day)
user_day.add_day()
print(user_day.day)

print(user_verse.daily_verse(user_day.day))