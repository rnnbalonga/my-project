import requests
import json
import datetime as dt

url = 'https://api.sunrise-sunset.org/json'

today = dt.datetime.now()

#Set parameters for API
#'lng' and 'lat' are currently set to Kawasaki's coordinates. Consider creating a constant for this instead.

parameters = {
    'lng' : 35.5223,
    'lat' : 139.7308,
    'formatted' : 0,
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)
print(today.hour)