#  if you want to scrape a website:

# 1 -> Use Api
# 2 -> Html web scraping using tool like bs4

# install all the requirement

import requests
import bs4
import html5lib

url = "https://codewithharry.com/"

# Step-1 Get the html

r = requests.get(url)         # it will save url request
html_content = r.content      # it will save content from that url request

# Step-2 Parse the html

soup = bs4.BeautifulSoup(html_content, "html.parser")       # it will parse the content
# print(soup.prettify())                                     # prettify is a function which will give proper indent
                                                             # to the content

# Step-3 Html tree traversal

# 1-Tag             print(title)
# 2-NavigableString -> print(title.string)
# 3-BeautifulSoup   ->print(soup)
# 4-comment

# Get the title of html page
title = soup.title

# Get all the paragraph for the page
paras = soup.find_all('p')
# print(paras)

# Get first paragraph for the page
# print(soup.find('p'))    # ->will give first paragraph
# print(soup.find('p')["class"])    # ->will give first paragraph class name
# print(soup.find("p").get_text())  # Get first paragraph text for the page
# print(soup.get_text())  # print the whole texted website



# Get all the anchor tag for the page
anchor = soup.find_all('a')
# print(anchor)

# get all the link s on the page
# all_links = set()     # will not repeated element
# for link in anchor:
#     if link.get('href') != '#':
#         Linktext = "https://codewithharry.com" + link.get('href')
#         all_links.add(Linktext)
#         print (all_links)


# Find all the element with class lead
# print(soup.find_all("p", class_="lead"))

navbarSupportContent = soup.find(id="navbarSupportedContent")
print(navbarSupportContent)
print ("-------------------------------------------")
for element in navbarSupportContent.contents:
    print (element)
