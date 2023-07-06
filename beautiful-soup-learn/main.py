from bs4 import BeautifulSoup 
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#Select individual elements
#print(soup.title)

#Print only the string inside a tag
#print(soup.h1.string)

#Print the entire html file + make it easier to read
#print(soup.prettify())

#Print all instances of a tag
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    #To get only the string of a tag, use below:
    #print(tag.getText())

    #To get hyperlinks:
    print(tag.get("href"))

#Using CSS selectors to select element

company_url = soup.select_one(selector="p a")
print(company_url)