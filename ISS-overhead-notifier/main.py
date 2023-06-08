import requests
import json
import datetime as dt

url = 'https://api.sunrise-sunset.org/json'

today = dt.datetime.now()

#Set parameters for API

parameters = {
    lng: 35.53,
    lat: 139.70,
    date: today,
}

response = requests.get(url)


