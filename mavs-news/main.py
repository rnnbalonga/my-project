from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get("https://www.mavsmoneyball.com/")
source = response.text

soup = BeautifulSoup(source, "lxml")

hero = soup.find('div', class_='c-six-up__main')

all_articles = [['Article Title', 'Author', 'Link']]

for article in hero.find_all('div', class_="c-entry-box--compact__body"):
    article_info = []
    article_info['article_title'] = article.h2.text
    article_info['article_author'] = article.find('span', class_="c-byline__author-name").text
    article_info['article_link'] = article.h2.a['href']
    
    all_articles.append(article_info)

print(all_articles)

#Generate a CSV with columns "Article", "Date Published", "Author", "Link"

