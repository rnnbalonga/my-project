from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

response = requests.get("https://www.mavsmoneyball.com/")
source = response.text

soup = BeautifulSoup(source, "lxml")

hero = soup.find('div', class_='c-six-up__main')

article_list = []

for article in hero.find_all('div', class_="c-entry-box--compact__body"):
    article_info = []
    rticle_title = article_info.append(article.h2.text)
    article_author = article_info.append(article.find('span', class_="c-byline__author-name").text)
    article_link = article_info.append(article.h2.a['href'])
    article_list.append(article_info)

# print(article_list)

all_articles = pd.DataFrame(article_list, columns=['Title', 'Author', 'Link'])

#Grab Date of Generated Report
today = datetime.date.today()
print(today)

#Generate a CSV with columns "Article", "Date Published", "Author", "Link"
all_articles.to_csv(f"{today}.csv", index= False)
