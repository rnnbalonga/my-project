import requests
import json
import datetime as dt

url = 'https://api.sunrise-sunset.org/json'

today = dt.datetime.now()

#Set parameters for API
#'lng' and 'lat' are currently set to Kawasaki's coordinates. Consider creating a constant for this instead.

parameters = {
    'lng' : 35.53,
    'lat' : 139.70,
}

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)