import requests
import json
import datetime as dt

#Sunrise & Sunset API
#Set Parameters
MY_LNG = 35.5223
MY_LAT = 139.7308

parameters = {
    'lng' : MY_LNG,
    'lat' : MY_LAT,
    'formatted' : 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

#Set Sunrise & Sunset
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

today = dt.datetime.now()

#

print(sunrise)
print(sunset)
print(today.hour)