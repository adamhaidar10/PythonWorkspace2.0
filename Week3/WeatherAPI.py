import requests
import json
import datetime

#   Dubai lat = 25.2048 lon = 55.2708
#   Riyadh lat = 24.7136  lon = 46.6753
#   Lusaka lat = 15.3875  lon = 28.3228° E
#   Tokyo lat = 35.6762  lon = 139.6503° E
#   Melbourne lat = 37.8136 lon = 144.9631° E
#   Seattle lat = 47.6062  lon = 122.3321
#   Buenos Aires lat = 34.6037 lon = 58.3816° W

def get_weather_reports(lat, lon):
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={float(lat)}&lon={float(lon)}&appid=4ae259d943afdda4f1b4fe60fa63a676"
    req = requests.get(endpoint)

    res_body = req.content.decode("utf-8")

    country_info = json.loads(res_body)


    temp = country_info["main"]["temp"]
    temp_c = float(temp) - 273.15

    weather = country_info["weather"][0]["main"]

    sunrise = country_info["sys"]["sunrise"]
    sunset = country_info["sys"]["sunset"]
    sunrise_time = datetime.datetime.fromtimestamp(sunrise)
    sunset_time = datetime.datetime.fromtimestamp(sunset)

    print(f"Temperature is {temp_c:.1f} C")
    print(f"Current weather is {weather}")
    print(f"Sunrise: {sunrise_time.strftime('%H:%M:%S')}")
    print(f"Sunset: {sunset_time.strftime('%H:%M:%S')}")

get_weather_reports(35.6762, 139.6503)

    

#     temp_in_c = float(report["main"]["temp"]) - 273.15
#     print(f"The Temperature in {city.capitalize()} is : {temp_in_c}")


# cities = {"duabi" :[25.2048, 55.2708],
#           "riyadh" :[24.7136, 46.6753],
#           "lusaka" :[15.3875, 28.3228],
#           "tokyo" :[35.6762, 139.6503],
#           "melbourne" :[37.8136, 144.963],
#           "seattle" :[47.6062, 122.3321],
#           "buenos Aires" :[34.6037, 58.3816]}

# for k, v in cities.items():
#     {get_weather(k, v)}
# res = requests.get(url)

# print(res.status_code)

# s = res.content.decode("utf-8")
# print(s)

# print("-----------")

# j = json.loads(s)
# print(j)

# print("-----------")


# temp = j["main"]["temp"]
# print(temp)

# temp_c = float(temp) - 273.15
# print(f"Temperature in Duabi is {temp_c} Celsius")

