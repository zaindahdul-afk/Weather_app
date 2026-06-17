import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = input("Enter city name: ").strip()

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params={"q": CITY, "appid": API_KEY, "units": "imperial"},
)

data = response.json()

if response.status_code != 200:
    print(f"Error: {data.get('message', 'Could not fetch weather data')}")
else:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].capitalize()
    city_name = data["name"]
    country = data["sys"]["country"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city_name}, {country}:")
    print(f"  Condition:  {description}")
    print(f"  Temp:       {temp}°F")
    print(f"  Feels like: {feels_like}°F")
    print(f"  Humidity:   {humidity}%")
    print(f"  Wind speed: {wind_speed} mph")
