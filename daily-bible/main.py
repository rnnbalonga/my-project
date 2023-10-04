from datetime import date
from day_counter import DayCounter
from verse_fetcher import VerseFetcher
from scraper import WebScraper
from discord.ext import commands
import schedule
import time
import discord
import os


user_day = DayCounter()
user_verse = VerseFetcher()
scraper = WebScraper()


def main ():
    current_date = str(date.today())
    origin_date = user_day.get_origin_date()

    if current_date != origin_date:
        #Manipulate the data in the last_run_date.txt file
        user_day.store_date(current_date)
        user_day.add_day()
        #Scrape verse & store output in today_verse.txt
        current_verse = user_verse.daily_verse(user_day.day) #output -> list
        scraper.collect_output_verse(current_verse)
    else:
        pass

def sched():
    main()

schedule.every().day.at("00:00").do(sched)

while True:
    schedule.run_pending()
    time.sleep(60)