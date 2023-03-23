import requests
from bs4 import BeautifulSoup

# set up the url of a web page
# url = "http://35.178.198.206/index.html"
# url = "http://35.178.198.206/bigpictures.html"
url = "http://35.178.198.206/styled.html"

# get the contents of the page
res = requests.get(url)
# check the status code (200 = success)
status_code = res.status_code
print(status_code)

# decode the contents of the page
html = res.content.decode("utf-8")
soup = BeautifulSoup(html, features="html.parser")

# find all the level 1 headers (h1) on the page
# (on a web page there should only be one h1 on a page)
headers = soup.find_all("h1")
for header in headers:
    print(header.get_text())

print("--------")

# find all the links on the page
links = soup.find_all("a")
#print(links)
for link in links:
    print(f"{link} : {link.get_text()} : {link.attrs['href']}")

print("--------")

# find all data that is styled with a particular class
c3 = soup.find_all("form", {"class" : "class3"})
print(c3)
for item in c3:
    print(item.get_text())