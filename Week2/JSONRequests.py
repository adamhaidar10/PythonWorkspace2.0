import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

res = requests.get(url)
#print(res.status_code)
#print(res.content)
print(res.headers["Content-Type"])

s = res.content.decode("utf-8")
todos = json.loads(s)
#print(s)

comp = []
todolist = []
for todo in todos:
    todolist.append(todo)
    if todo["completed"] == True:
        comp.append(todo)
    if todo["id"] == 50:
        print(todo)
print(f"there are {len(todolist)} items of which {len(comp)} are finished")

