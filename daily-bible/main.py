from day_counter import DayCounter
from verse_fetcher import VerseFetcher

user_day = DayCounter()
user_verse = VerseFetcher()

day = user_day.day
today_verse = user_verse.daily_verse(day)
for verse in today_verse:
    print(verse)