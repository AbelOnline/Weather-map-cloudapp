import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()

def kelvin_to_celsius_farhenheit(kelvin):
    celsius = kelvin - 273.15
    farhenheit = (celsius * 9/5) + 32
    return celsius, farhenheit

def get_weather_data(city):
    try:
        url = f"{BASE_URL}appid={API_KEY}&q={city}"
        
        response = requests.get(url)
        
        # 200 si la réponse réussie sinon erreur 
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Exception as e:
        print(f"Erreur inattendue : {str(e)}")
        return None

def print_weather_info(city, data):
    if data is not None:
        temp_kelvin = data['main']['temp']
        temp_celsius, temp_farheinhet = kelvin_to_celsius_farhenheit(temp_kelvin)
        feels_like_kelvin = data['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_farhenheit(feels_like_kelvin)
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temp_celsius:.2f}°C or {temp_farheinhet:.2f}°F")
        print(f"Feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")
        print(f"Description: {description}")
        print(f"Sunrise time: {sunrise_time} (local time)")
        print(f"Sunset time: {sunset_time} (local time)")
    else:
        print(f"Erreur lors de la récupération des données météorologiques pour {city}.")

# Liste des cinq villes
cities = ["Paris", "Addis Abeba", "Londres", "Sydney", "New York"]

# Récupérer et afficher les données météorologiques pour chaque ville de la liste
for city in cities:
    data = get_weather_data(city)
    print_weather_info(city, data)
