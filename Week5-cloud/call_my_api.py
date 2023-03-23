import requests
import json

# url = "http://127.0.0.1:8000/cube?n=8"
url = "http://20.104.232.32:8000/cube?n=22"
res = requests.get(url)

print(res.content.decode("utf-8"))
