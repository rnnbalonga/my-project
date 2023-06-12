import requests

URL = "https://api.openweathermap.org/data/3.0/onecall?"

parameters = {
    'lng' : 139.7029,
    'lat' : 35.5308,
    'appid': "98f54ab1014ca867c1a5d590939ca4d9"
    'exclude' "currently,minutely,daily"
}

response = requests.get(URL, params=parameters)
print(response.status_code)