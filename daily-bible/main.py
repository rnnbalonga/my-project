from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from scraper import WebScraper


# from discord_bot import DiscordBot

user_day = DayCounter()
user_verse = VerseFetcher()


#Get user_verse list from user_day
current_verse = user_verse.daily_verse(user_day.day)
print(current_verse[2])


#Scrape verse from current_verse


scraper = WebScraper()

# #Test 1 verse
# #scraper.scrape_verse(current_verse[0])

# #Consider saving the scraped verses into a variable which can be accessed later. Create a list of dictionaries where book-chapter is the key and the passage is the value.
current_day_output = []

# #Loop through all items in list
for verse in current_verse:
    current_verse_output = {}
    current_verse_output['reference'] = verse
    current_verse_output['verse'] = scraper.scrape_verse(verse)
    current_day_output.append(current_verse_output)

scraper.quit()

print(len(current_day_output))


#Consider showing a message in the console that {passage} has been saved.
#Browser should only close after all passages have been successfully scraped

# for verse in current_verse:
#     scraper.scrape_verse(verse)