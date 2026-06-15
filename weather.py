import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Los Angeles"

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": CITY, "appid": API_KEY, "units": "metric"},
)

data = response.json()
print(data)
