import requests
import json
import datetime as dt

MY_LONG = 35.5223
MY_LAT = 139.7308

today = dt.datetime.now()
current_hour = today.hour

#Sunrise & Sunset API
parameters = {
    'lng' : MY_LONG,
    'lat' : MY_LAT,
    'formatted' : 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

#ISS API
iss_response = requests.get('http://api.open-notify.org/iss-now.json')
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_longitude = float(iss_data['iss_position']['longitude'])
iss_latitude = float(iss_data['iss_position']['latitude'])


##### FUNCTIONS #####

#Check if ISS postion is close to my current location

def iss_location_check():
    '''
    This function checks if the ISS is within 5 deg of my coordinates.
    '''
    long_diff = abs(MY_LONG - iss_longitude)
    lat_diff = abs(MY_LAT - iss_latitude)
    if long_diff <= 5 and lat_diff <=5:
        return True
    else:
        return False

#Check if it's currently dark

def check_dark():
    '''
    This function checks if current hour is between sunset and sunrise.
    '''
    if current_hour < sunrise or current_hour > sunset:
        return True
    else:
        return False

def send_mail():
    '''
    If both iss_location_check and check_dark return TRUE, an email will be sent.
    '''


iss_location_check()
check_dark()