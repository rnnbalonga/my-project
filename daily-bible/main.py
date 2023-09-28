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


def main ():
    current_date = str(date.today())
    origin_date = user_day.get_origin_date()

    if not user_day.compare_dates(current_date=current_date, origin_date=origin_date):
        user_day.store_date(current_date)
        user_day.add_day()

    current_verse = user_verse.daily_verse(user_day.day)

    current_day_output = []

    scraper.open_site()

    current_day_output = [{'reference': verse, 'verse': scraper.scrape_verse(verse)} for verse in current_verse]

    for output in current_day_output:
        print(output['reference'])
        print("\n")
        print(output['verse'])
        
    scraper.quit()

    print(current_day_output)


main()