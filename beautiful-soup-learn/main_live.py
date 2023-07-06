from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

#Find all anchor tags
article = soup.find(name="span", class_="titleline")
article_title = soup.select(".titlelink a")
print(article_title)