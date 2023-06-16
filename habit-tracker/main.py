import requests

USERNAME = "nikebalonga"
TOKEN = "29b2f8302a75c6bbbccc0867ba79ad8e"
GRAPH_ID = "q1c1b0f4b2302ca3"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Habit",
    "unit": "Days",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_create_config = {
    "date" : "20230616",
    "quantity": "1"
}

#Create Graph
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

#Post
response = requests.post(url=pixel_create_endpoint,headers=headers,json=pixel_create_config)
print(response.text)

print(pixel_create_endpoint)