import requests
import json
import datetime as dt
import smtplib

MY_LONG = 139.7029
MY_LAT = 35.5308

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

#Email settings
my_email = "ruben.lingito@gmail.com"
password = "kizszdeyikbdrhig"


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
    jp_sunrise = (sunrise + 9) % 24
    jp_sunset = (sunset + 9) % 24
    if current_hour < jp_sunrise or current_hour > jp_sunset:
        return True
    else:
        return False

def send_mail():
    '''
    If both iss_location_check and check_dark return TRUE, an email will be sent.
    '''
    if iss_location_check() and check_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, 
                                        to_addrs="nikebalonga@gmail.com", 
                                        msg=f"ISS Location Report\n\nYou might be able to see the ISS above you. Check outside!\nKind regards,\nNike")
    else:
        print("EGULS LODS")

send_mail()