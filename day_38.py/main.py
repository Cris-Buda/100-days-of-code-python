import requests
from datetime import datetime

APP_ID = '...'
API_KEY = '...'

NUTRITIONX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = " "
WEIGHT_KG =
HEIGHT_CM =
AGE =

SHEET_ENDPOINT = "https://api.sheety.co/a2a0629231450ac8ec6cd1d467083a5d/myWorkoutsIncaUnu/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("Tell me which exercises you did: ")
# exercise_text = "run"

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONX_ENDPOINT, json=parameters, headers=headers)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
"Authorization": "..."
}

sheet_response = requests.post(url="https://api.sheety.co/a2a0629231450ac8ec6cd1d467083a5d/myWorkoutsIncaUnu/workouts", json=sheet_inputs, headers=bearer_headers)
print(sheet_response.status_code)