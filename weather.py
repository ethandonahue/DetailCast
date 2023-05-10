from config import api_key
import requests

def get_weather(location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

    response = requests.get(url)
    print(response.json())

    # temperature_c = response.json()['current']['temp_c']  # Temperature in Celsius
    temperature_f = response.json()['current']['temp_f']  # Temperature in Fahrenheit

    return temperature_f

    # Print the temperature in Celsius and Fahrenheit
    # print(f'Temperature in {location}: {temperature_c}°C ({temperature_f}°F)')
