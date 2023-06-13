import requests

# URL = "https://api.openweathermap.org/data/3.0/onecall?"

# parameters = {
#     'lng' : 139.7029,
#     'lat' : 35.5308,
#     'appid': "98f54ab1014ca867c1a5d590939ca4d9",
#     'exclude': "currently,minutely,daily"
# }

URL = "http://api.weatherapi.com/v1/forecast.json?"

parameters = {
    'key': "ee3ea6f07fc14926a0c120639231306",
    'q': "35.5308,139.7029",
    'days': 2,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['forecast']['forecastday'][0]['hour'][:12]

will_rain = False

for hour_data in weather_slice:
    will_it_rain = hour_data['will_it_rain']
    if will_it_rain == 1:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
else:
    print("lmao")

# print(weather_data['forecast']['forecastday'][0]['day']['daily_will_it_rain'])