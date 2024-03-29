import requests
import datetime as dt

USERNAME = "nikebalonga"
TOKEN = "29b2f8302a75c6bbbccc0867ba79ad8e"
GRAPH_ID = "q1c1b0f4b2302ca3"

date = dt.datetime(2023,6,12)
date_format = date.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_format}"
print(f"{graph_endpoint}/{GRAPH_ID}")


headers = {
    "X-USER-TOKEN": TOKEN
}

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

graph_update_config = {
    "name" : "Eat. Sleep. Code.",
    "unit" : "Lessons"
}

pixel_post_config = {
    "date" : date_format,
    "quantity" : str(input("How many lessons did you do today?: ")),
}

pixel_update_config = {
    "quantity" : '7',
}


#Create Graph

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

#Update Graph

# response = requests.put(url=graph_update_endpoint, headers=headers, json=graph_update_config)
# print(response.text)

#Post a Pixel

response = requests.post(url=pixel_create_endpoint,headers=headers,json=pixel_post_config)
print(response.text)

# Update Pixel
# REMINDER: ALWAYS CHECK THE TYPE OF REQUEST

# response = requests.put(url=pixel_update_endpoint, headers=headers, json=pixel_update_config)
# print(response.text)

#Delete a pixel

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)