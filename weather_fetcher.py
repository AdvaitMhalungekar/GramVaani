import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"

def get_current_weather(location):
    url = f"{BASE_URL}/current.json?key={API_KEY}&q={location}"
    response = requests.get(url)
    return response.json()

def get_forecast(location, days=3, alerts="yes", aqi="yes"):
    url = f"{BASE_URL}/forecast.json?key={API_KEY}&q={location}&days={days}&alerts={alerts}&aqi={aqi}"
    response = requests.get(url)
    return response.json()

def get_alerts(location):
    url = f"{BASE_URL}/alerts.json?key={API_KEY}&q={location}"
    response = requests.get(url)
    return response.json()

def simplify_forecast_data(data):
    simplified = []

    for day_data in data['forecast']['forecastday']:
        day_summary = {
            "date": day_data['date'],
            "max_temp_c": day_data['day']['maxtemp_c'],
            "min_temp_c": day_data['day']['mintemp_c'],
            "avg_temp_c": day_data['day']['avgtemp_c'],
            "condition": day_data['day']['condition']['text'],
            "icon": day_data['day']['condition']['icon'],
            "sunrise": day_data['astro']['sunrise'],
            "sunset": day_data['astro']['sunset'],
            "hourly_data": []
        }

        # Sort hourly data by time (already sorted usually, but just to be safe)
        sorted_hours = sorted(day_data['hour'], key=lambda h: h['time'])

        for hour in sorted_hours:
            hour_summary = {
                "time": hour['time'],
                "temp_c": hour['temp_c'],
                "condition": hour['condition']['text'].strip(),
                "icon": hour['condition']['icon'].strip(),
                "humidity": hour['humidity'],
                "wind_kph": hour['wind_kph'],
                "air_quality": {
                    "pm2_5": hour.get("air_quality", {}).get("pm2_5"),
                    "pm10": hour.get("air_quality", {}).get("pm10"),
                    "co": hour.get("air_quality", {}).get("co")
                }
            }
            day_summary["hourly_data"].append(hour_summary)

        simplified.append(day_summary)
        simplified.append(data['alerts'])

    return simplified

def get_weather_data(location):
    forecast_raw = get_forecast("Kolhapur", days=3, alerts="yes", aqi="yes")
    forecast_simplified = simplify_forecast_data(forecast_raw)
    return forecast_simplified
