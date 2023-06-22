import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
TOKEN = os.environ['TOKEN']

#ENDPOINTS
natural_exercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_post_endpoint = "https://api.sheety.co/0306c09badd8a97583ca2bcadecfe47d/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Authorization": f'Bearer {TOKEN}',
}

exercise_post_config = {
    "query": str(input("What exercise did you do today?: ")),
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 167,
    "age": 29
}


#Post an exercise
natural_exercise_response = requests.post(url=natural_exercise_endpoint,headers=headers,json=exercise_post_config)
exercise_json = natural_exercise_response.json()
# print(exercise_json)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in exercise_json["exercises"]:
    sheety_post_config = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }   
    }

    # Post a row on Google Sheets
    sheety_response = requests.post(url=sheety_post_endpoint,json=sheety_post_config)
    # print(sheety_response.status_code)