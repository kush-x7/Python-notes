from bs4 import BeautifulSoup
# import lxml  if html parser dont work than use lsml istead of html.parser

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.prettify())

print (soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector="p a")


company_url = soup.select_one("#name")


company_url = soup.select(".heading")
