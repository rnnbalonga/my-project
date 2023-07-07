from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.mavsmoneyball.com/")
source = response.text

soup = BeautifulSoup(source, "lxml")

hero = soup.find('div', class_='c-six-up')


article = hero.h2.text
article_link = hero.h2
print(article)

