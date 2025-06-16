import requests as req
from dotenv import load_dotenv
from os import getenv
from sys import argv

def getLatitudeAndLongitude(api_key, location):
    res = req.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}')
    if res.status_code != 200:
        print(f'Location "{location}" not found.')
        return
    data = res.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    return lat, lon

def getWeather(api_key, lat, lon):
    res = req.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
    if res.status_code != 200:
        print('Error: coulnd\'t get the weather at that location.')
        print(res.status_code)
        return
    data = res.json()
    return data

def main():
    if len(argv) == 1:
        print('You must provide 1 argument. Run \'weather -h\' for help.')
        return
    
    if argv[1] == '-v' or argv[1] == '--version':
        print('weather v1.0.0')
        return
    
    if argv[1] == '-h' or argv[1] == '--help':
        print('Help\n')
        print('1. weather -h')
        print('2. weather -v')
        print('3. weather <location>')
        return
    
    load_dotenv()
    api_key = getenv("WEATHER_API_KEY")

    location = argv[1]

    lat, lon = getLatitudeAndLongitude(api_key, location)
    weather_data = getWeather(api_key, lat, lon)

    name = weather_data['name']
    weather = weather_data['weather'][0]['main']
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    emojis = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️',
        'Smoke': '🌫️',
        'Dust': '🌪️',
        'Sand': '🌪️',
        'Ash': '🌋',
        'Squall': '🌪️',
        'Tornado': '🌪️'
    }

    print(f'\n📍 {name}\n')
    print(f'{emojis[weather]} {weather}')
    print(f'🌡️ {round(temperature - 273.15)}°C, feels like {round(feels_like - 273.15)}°C')
    print(f'💧 {humidity}%')
    print(f'💨 {wind_speed}m/s')

if __name__ == '__main__':
    main()