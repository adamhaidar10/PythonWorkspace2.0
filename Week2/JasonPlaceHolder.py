import requests
import json
# set url
url = "https://jsonplaceholder.typicode.com/posts?userId=4"
# call the service
res = requests.get(url)
# display the headers
print(res.headers["Content-Type"])
# print("---------------------")
# # decode
s = res.content.decode("utf-8")

# turns string into list with json.loads
posts = json.loads(s)
print(posts[0]["title"])
print(type(s))

print("-----------------")
# loop through and prints title
for post in posts:
    print(post["title"])
