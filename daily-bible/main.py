from datetime import date
from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from scraper import WebScraper

user_day = DayCounter()
user_verse = VerseFetcher()
scraper = WebScraper()


def scrape_verse():
    current_verse = user_verse.daily_verse(user_day.day)

    #Consider saving the scraped verses into a variable which can be accessed later. Create a list of dictionaries where book-chapter is the key and the passage is the value.
    current_day_output = []

    scraper.open_site()

    #Loop through all items in list
    for verse in current_verse:
        current_verse_output = {}
        current_verse_output['reference'] = verse
        current_verse_output['verse'] = scraper.scrape_verse(verse)
        current_day_output.append(current_verse_output)

    scraper.quit()

    for output in current_day_output:
        print(output)
        print("\n")

    #Call add_day method when current date is changed
    current_date = str(date.today())
    origin_date = ""

    if current_date != origin_date:
        origin_date = current_date
        user_day.add_day()
    else:
        pass

scrape_verse()

