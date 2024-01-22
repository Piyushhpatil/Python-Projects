import requests
from datetime import datetime
import os

API_KEY = os.environ["APP_ID"]
APP_ID = "f1b6afe2"

SHEET_KEY = "dslknfjlsficqnqiwcqwiomefdosf3039rf"

sheets_enpoint = "https://api.sheety.co/853693dfc331fc8236940a76c0e6c129/myWorkout/workouts"
excersise_enpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers ={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
auth = {
    "Authorization": f"Bearer {SHEET_KEY}"
}
# input("What Excercise have you done today?")


excersise_content = {
    "query": input("What exercise have you done today?"),
    "gender": "male",
    "weight_kg": 98,
    "height_cm": 180,-
    "age": 20,
}

today = datetime.now()
datee = today.strftime("%d/%m/%Y")
timee = today.strftime("%H:%M:%S")

response = requests.post(url=excersise_enpoint, json=excersise_content, headers=headers)
results = response.json()["exercises"]


for result in results:
    sheet = {
        "workout": {
            "date": datee,
            "time": timee,
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheets_enpoint, json=sheet, headers=auth)
    print(sheet_response.text)




