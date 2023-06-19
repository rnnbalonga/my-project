import requests

APP_ID = "3ef3941b"
APP_KEY = "18a1fd58ed4bc36ec5d39d25b6d2d44a"

natural_exercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_post_config = {
    "query": str(input("What exercise did you do today?: ")),
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 167,
    "age": 29
}

response = requests.post(url=natural_exercise_endpoint,headers=headers,json=exercise_post_config)
print(response.text)