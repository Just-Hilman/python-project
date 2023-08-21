import requests

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?"