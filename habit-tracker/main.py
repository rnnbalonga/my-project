import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "29b2f8302a75c6bbbccc0867ba79ad8e",
    "username": "nikebalonga",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)