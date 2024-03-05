# main.py
from fastapi import FastAPI
import requests

app = FastAPI()

OPENWEATHERMAP_API_KEY = "80a092e52cf3895fd6541d2a0e35ade9"

def fetch_weather_data(city: str, days: int):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={days}&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

@app.get("/temperature")
async def get_temperature():
    city = "Lisbon"
    days = 3
    weather_data = fetch_weather_data(city, days)
    if weather_data:
        temperature_kelvin = weather_data['list'][0]['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15  # Conversion from Kelvin to Celsius
        return {"temperature": round(temperature_celsius, 2)}  # Rounding to 2 decimal places
    else:
        return {"error": "Failed to fetch weather data"}

@app.get("/rain")
async def get_rain():
    city = "Lisbon"
    days = 3
    weather_data = fetch_weather_data(city, days)
    if weather_data:
        for forecast in weather_data['list']:
            if 'rain' in forecast:
                return {"rain": True}
        return {"rain": False}
    else:
        return {"error": "Failed to fetch weather data"}