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


scraper = WebScraper()

#Test 1 verse
# scraper.scrape_verse(current_verse[0])

#Loop through all items in list
#Consider saving the scraped verses into a variable which can be accessed later. Create a dictionary where book-chapter is the key and the passage is the value.
#Consider showing a message in the console that {passage} has been saved.
#Browser should only close after all passages have been successfully scraped

# for verse in current_verse:
#     scraper.scrape_verse(verse)