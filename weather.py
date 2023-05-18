from static.config import api_key
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
    uv = response.json()['current']['uv']
    day = response.json()['current']['is_day']
    # time = response.json()['current']['localtime']
    # time_part = time.split()[1]

    tempScore = 0.0

    if 70.0 <= temp <= 73.0:
        tempScore = 100.0
    elif 68.0 <= temp < 70.0 or 73.0 < temp <= 75.0:
        tempScore = 90.0
    elif 66.0 <= temp < 68.0 or 75.0 < temp <= 77.0:
        tempScore = 80.0
    elif 64.0 <= temp < 66.0 or 77.0 < temp <= 79.0:
        tempScore = 70.0
    elif 62.0 <= temp < 64.0 or 79.0 < temp <= 81.0:
        tempScore = 60.0
    elif 60.0 <= temp < 62.0 or 81.0 < temp <= 83.0:
        tempScore = 50.0
    elif 58.0 <= temp < 60.0 or 83.0 < temp <= 85.0:
        tempScore = 40.0
    elif 56.0 <= temp < 58.0 or 85.0 < temp <= 87.0:
        tempScore = 30.0
    elif 54.0 <= temp < 56.0 or 87.0 < temp <= 89.0:
        tempScore = 20.0
    else:
        tempScore = 10.0

    cloudScore = clouds

    # Cloud Coverage
    if uv <= 2.0:
        cloudScore = 100.0
    # else:
    #     if 80.0 <= clouds <= 100.0:
    #         cloudScore = 100.0
    #     elif 50.0 <= clouds < 80.0:
    #         cloudScore = 60.0
    #     elif 25.0 <= clouds < 50.0:
    #         cloudScore = 30.0
    #     else:
    #         cloudScore = 10.0

    windScore = 0.0

    # Wind Conditions
    if 6.0 <= wind <= 12.0:
        windScore = 100.0
    elif 0.0 <= wind < 6.0:
        windScore = 80.0
    elif 13.0 <= wind <= 20.0:
        windScore = 30.0
    else:
        windScore = 0


    print(tempScore, windScore, cloudScore)
    print((tempScore + windScore + cloudScore)/3)
    combinedScore = (tempScore + windScore + cloudScore) / 3

    if precip >= 10 or day == 0:
        combinedScore = 0



    if combinedScore >= 90.0:
        washingRecommendation = "excellent conditions for car washing."
    elif combinedScore >= 70.0:
        washingRecommendation = "good conditions for car washing."
    elif combinedScore >= 50.0:
        washingRecommendation = "fair conditions for car washing."
    else:
        washingRecommendation = "not ideal conditions for car washing."

    print(washingRecommendation)
    # print(grade)

    return washingRecommendation

    # Print the temperature in Celsius and Fahrenheit
    # print(f'Temperature in {location}: {temperature_c}°C ({temperature_f}°F)')
