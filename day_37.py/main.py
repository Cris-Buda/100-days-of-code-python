import requests
from datetime import datetime

from dateutil.utils import today

USERNAME = "abc"
TOKEN = "..."
GRAPH_ID = "..."
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graf_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graf_params = {
    "id": GRAPH_ID,
    "name": "learningPython Graf",
    "unit": "h",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graf_endpoint, json=graf_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2025, month=2, day=20)
# print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you learn Python today?")
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(pixel_response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

update_params = {
     "quantity": "8"
}

# update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_response.text)

# delete_response = requests.delete(url=update_endpoint, json=update_params, headers=headers)