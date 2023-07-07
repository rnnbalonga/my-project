from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.mavsmoneyball.com/")
source = response.text

soup = BeautifulSoup(source, "lxml")

hero = soup.find('div', class_='c-six-up')


article = hero.h2.text
article_link = hero.h2.a['href']
article_author = hero.find('span', class_="c-byline__author-name").text
print(article)
print(article_link)
print(article_author)

