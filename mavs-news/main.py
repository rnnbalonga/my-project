from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.mavsmoneyball.com/")
source = response.text

soup = BeautifulSoup(source, "lxml")

hero = soup.find('div', class_='c-six-up__main')

for article in hero.find_all('div', class_="c-entry-box--compact__body"):
    article_title = article.h2.text
    article_link = article.h2.a['href']
    article_author = article.find('span', class_="c-byline__author-name").text
    print(article_title)
    print(article_link)
    print(article_author)
    print('\n')

