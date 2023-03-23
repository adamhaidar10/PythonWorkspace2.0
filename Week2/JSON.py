import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)
print(res.status_code)
#print(res.content)
print(res.headers["Content-Type"])

userlist = res.content.decode("utf-8")

users = json.loads(userlist)
print(type(userlist))

for user in users:
    print(f'{user["name"]} , {user["email"]}')

#add city tough challenge part