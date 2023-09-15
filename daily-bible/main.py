from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from scraper import WebScraper


# from discord_bot import DiscordBot

user_day = DayCounter()
user_verse = VerseFetcher()


#Get user_verse list from user_day
current_verse = user_verse.daily_verse(user_day.day)
print(type(current_verse[0]))

#Scrape verse from current_verse

#Test 1 verse
scraper = WebScraper()
scraper.scrape_verse(current_verse[0])

