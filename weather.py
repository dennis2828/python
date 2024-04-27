import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    city = input("\nEnter a city: \n")
    request_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&q={city}&appid={os.getenv("API_KEY")}"

    weather_data = requests.get(request_url).json()

    pprint(weather_data)