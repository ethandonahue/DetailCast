from config import api_key
import requests


def get_weather(location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

    response = requests.get(url)
    print(response.json())

    if 'error' in response.json():
        return 'error'

    # temperature_c = response.json()['current']['temp_c']  # Temperature in Celsius
    temp = response.json()['current']['temp_f']  # Temperature in Fahrenheit
    clouds = response.json()['current']['cloud']
    wind = response.json()['current']['wind_mph']
    precip = response.json()['current']['precip_mm']

    score = 0

    if temp < 50 or temp > 80:
        pass
    elif (50 <= temp <= 59) or (70 <= temp <= 80):
        score += 1
    else:
        score += 2

    # Cloud coverage
    if clouds < 20:
        pass
    elif clouds <= 50:
        score += 1
    else:
        score += 2

    # Precipitation
    if precip > 2.5:
        pass
    elif precip >= 0.1:
        score += 1
    else:
        score += 2

    # Wind
    if wind > 20:
        pass
    elif wind >= 10:
        score += 1
    else:
        score += 2

    if score == 8:
        grade = "A+"
    elif score == 7:
        grade = "A"
    elif score == 6:
        grade = "A-"
    elif score == 5:
        grade = "B+"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    else:
        grade = "F"

    print(temp, clouds, wind, precip)
    print(score)
    print(grade)

    return temp

    # Print the temperature in Celsius and Fahrenheit
    # print(f'Temperature in {location}: {temperature_c}°C ({temperature_f}°F)')
