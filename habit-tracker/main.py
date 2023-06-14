import requests

USERNAME = "nikebalonga"
TOKEN = "29b2f8302a75c6bbbccc0867ba79ad8e"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": "q1c1b0f4b2302ca3",
    "name": "Coding Habit",
    "unit": "Days",
    "type": "int",
    "color": "shibafu",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

response = requests.post(url=graph_endpoint,json=graph_config)
print(response.text)