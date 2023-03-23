import json
import requests
import shutil
from datetime import datetime, timedelta

url = "https://api.nasa.gov/planetary/apod?api_key=xT4SNawH7m7OLbbOwb1IN0MAq8zNoaHsKRDu66al"
asteroid_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={datetime.now().strftime('%Y-%m-%d')}&end_date={datetime.now().strftime('%Y-%m-%d')}&api_key=xT4SNawH7m7OLbbOwb1IN0MAq8zNoaHsKRDu66al"

def get_json(url):
    response = requests.get(url)
    s_res = response.content.decode("utf-8")
    return json.loads(s_res)
    

def get_pic_of_day(apod):
    img_title = apod["title"]
    img_hd = requests.get(apod["url"], stream=True)

    outfile = open(f"{img_title}.png", "wb")
    shutil.copyfileobj(img_hd.raw, outfile)
    outfile.close()

def get_10_days():
    date_to = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d') # 10 prints 11
    
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=xT4SNawH7m7OLbbOwb1IN0MAq8zNoaHsKRDu66al&start_date={date_to}")
    s_res = response.content.decode("utf-8")
    img_array = json.loads(s_res)

    for img in img_array: # can also do range
        img_hd = requests.get(img["url"], stream=True)

        outfile = open(f"{img['date']},{img['title']}.png", "wb")
        shutil.copyfileobj(img_hd.raw, outfile)
        outfile.close()

def get_danger(asteroids):
    n_e_objs = asteroids["near_earth_objects"][datetime.now().strftime('%Y-%m-%d')]

    for i in n_e_objs:
         if i["is_potentially_hazardous_asteroid"] == True:
             print(f"Asteroid ID: {i['id']}, Name: {i['name']}")
       


print("Task 1----------------------------------------------------------------|||")
get_pic_of_day(get_json(url))
get_10_days()

print("Task 2----------------------------------------------------------------|||")
get_danger(get_json(asteroid_url))

import requests
import json

# set the date
d = "2023-02-06"

# call the api
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={d}&end_date={d}&api_key=DEMO_KEY"
ret = requests.get(url)
# print(ret.status_code)

# extract the json
retdata = ret.content.decode("utf-8")
print(retdata)
jsondata = json.loads(retdata)

# how many asteroids are near earth today?
elementcount = jsondata["element_count"]
print(f"{elementcount} asteroids near earth today...")

# check to see if any of the asteroids are hazardous
for object in jsondata["near_earth_objects"][d]:
    # print(object)
    name = object["name"]
    hazardous = object["is_potentially_hazardous_asteroid"]
    print(f"Object {name} : hazardous? {hazardous}")