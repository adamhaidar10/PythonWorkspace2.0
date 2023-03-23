import requests
import json

url = "https://jsonplaceholder.typicode.com/todos?id=50"

res = requests.get(url)
print(res.status_code)
print(res.content)
print(res.headers["Content-Type"])

s = res.content.decode("utf-8")
print(s)
