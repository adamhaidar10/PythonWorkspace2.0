import requests
import json

# locations - city name, latitude, longitude (found from google)
locations = [
    ("London", 51.5072, 0.1276),
    ("Tokyo", 35.6762, 139.6503),
    ("Lusaka", -15.3875, 28.3228),
    ("Lima", -12.0464, -77.0428),
    ("Ottawa", 45.4215, -75.6972),
    ("Riyadh", 24.7136, 46.6753)
    ]

print("WORLD WEATHER REPORT")

for location in locations:
    city = location[0]
    lat = location[1]
    lon = location[2]

    # substitute lat and lon into url of api
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=71f80dc0cf159350230084558983a51c"

    # call the api
    ret = requests.get(url)

    # turn the response data into json
    decodeddata = ret.content.decode("UTF-8")
    jsondata = json.loads(decodeddata)

    # extract the main weather type from the json
    mainweather = jsondata["weather"][0]["main"]
    temp = float(jsondata["main"]["temp"]) - 273.15

    # format the output
    print(f"{city} : {mainweather} : {temp:.2f}")