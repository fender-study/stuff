import requests
import datetime as dt
import os

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("Enter exercise: ")

parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 170,
    "age": 69
}
response = requests.post(url=ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
nutri_data = response.json()

exercise = []
durations = []
calories = []
for item in nutri_data['exercises']:
    exercise.append(item['name'])
    durations.append(item['duration_min'])
    calories.append(item['nf_calories'])


GOOGLE_SHEET_ENDPOINT_GET = "https://api.sheety.co/82c330a4d11c56a759515671737c4015/myWorkout/аркуш1"
GOOGLE_SHEET_ENDPOINT_POST = "https://api.sheety.co/82c330a4d11c56a759515671737c4015/myWorkout/аркуш1"

current_date = dt.datetime.now()
date = current_date.strftime("%d/%m/%Y")
time = current_date.now().strftime("%H:%M")
for i in range(len(exercise)):
    data = {
        "аркуш1": {
            "date": date,
            "time": time,
            "exercise": exercise[i],
            "duration": durations[i],
            "calories": calories[i]
        }
    }
    google_response = requests.post(url=GOOGLE_SHEET_ENDPOINT_POST, json=data)
    google_response.raise_for_status()
    print(google_response.status_code)
    print(google_response.text)
