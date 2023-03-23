import requests
from bs4 import BeautifulSoup
import re

# get a page, parse it
url = "http://35.178.198.206/index.html"
ret = requests.get(url)
txt = ret.content.decode("utf-8")
# print(txt)
soup = BeautifulSoup(txt, features="html.parser")

# find all the h2 items
print(soup.find_all("h2"))

print("-------------------------------------")

# show just the text from the H2 items
hdrs = soup.find_all("h2")
for hdr in hdrs:
    print(hdr.get_text())

print("-------------------------------------")

# find all the links in the downloaded page
links = soup.find_all("a")
for link in links:
    print("{} : {}".format(link.get_text(), link.attrs["href"]))

print("-------------------------------------")

# get another page, find all the Watson quotes
url = "http://35.178.198.206/scarlet1.html"
ret = requests.get(url)
txt = ret.content.decode("utf-8")
soup = BeautifulSoup(txt, features="html.parser")
watsonquotes = soup.find_all("span", {"class": "watson"})
for quote in watsonquotes:
    print(quote.get_text())

print("-------------------------------------")

# find all the links to pictures on a page using a regular expression
reg = re.compile(".*.jpg")
url = "http://35.178.198.206/bigpictures.html"
ret = requests.get(url)
txt = ret.content.decode("utf-8")
soup = BeautifulSoup(txt, features="html.parser")
links = soup.find_all("a", {"href": reg})
# print(links)
for link in links:
    print("{}".format(link.attrs["href"]))

# loop through the links
for link in links:
    # construct a full url
    picurl = "http://35.178.198.206/" + link.attrs["href"]
    print(picurl)

    # get the picture contents
    ret = requests.get(picurl)

    # write the contents to a file
    outfile = open(link.attrs["href"], "wb")
    outfile.write(ret.content)
    outfile.close()
