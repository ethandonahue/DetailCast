from static.config import api_key
import datetime
import requests


def get_weather(location):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=3"

    response = requests.get(url)
    forecast_data = response.json()

    if 'error' in forecast_data:
        return 'error'

    recommendations = []

    for forecast in forecast_data['forecast']['forecastday']:
        date = forecast['date']
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A %m/%d")
        daily_recommendations = []
        for hour in forecast['hour']:
            time = datetime.datetime.strptime(hour['time'], "%Y-%m-%d %H:%M")
            time = time.strftime("%I:%M %p").lstrip("0")  # Remove leading zero using lstrip()
            temp = hour['temp_f']
            clouds = hour['cloud']
            wind = hour['wind_mph']
            precip = hour['precip_mm']
            uv = hour['uv']
            day = hour['is_day']

            tempScore = calculate_temp_score(temp)
            cloudScore = calculate_cloud_score(clouds, uv)
            windScore = calculate_wind_score(wind)
            combinedScore = calculate_combined_score(tempScore, cloudScore, windScore, precip, day)

            print(date, time, tempScore, cloudScore, windScore)

            washingRecommendation = get_washing_recommendation(combinedScore)

            if washingRecommendation != "":
                daily_recommendations.append({
                    'time': time,
                    'washing_recommendation': washingRecommendation,
                })

        recommendations.append({
            'date': formatted_date,
            'daily_recommendations': daily_recommendations
        })

    return recommendations


def calculate_temp_score(temp):
    # Temperature Score Calculation
    if 70.0 <= temp <= 73.0:
        return 100.0
    elif 68.0 <= temp < 70.0 or 73.0 < temp <= 75.0:
        return 90.0
    elif 66.0 <= temp < 68.0 or 75.0 < temp <= 77.0:
        return 80.0
    elif 64.0 <= temp < 66.0 or 77.0 < temp <= 79.0:
        return 70.0
    elif 62.0 <= temp < 64.0 or 79.0 < temp <= 81.0:
        return 60.0
    elif 60.0 <= temp < 62.0 or 81.0 < temp <= 83.0:
        return 50.0
    elif 58.0 <= temp < 60.0 or 83.0 < temp <= 85.0:
        return 40.0
    elif 56.0 <= temp < 58.0 or 85.0 < temp <= 87.0:
        return 30.0
    elif 54.0 <= temp < 56.0 or 87.0 < temp <= 89.0:
        return 20.0
    else:
        return 10.0


def calculate_cloud_score(clouds, uv):
    # Cloud Score Calculation
    if uv <= 2.0:
        return 100.0
    return clouds


def calculate_wind_score(wind):
    # Wind Score Calculation
    if 6.0 <= wind <= 12.0:
        return 100.0
    elif 0.0 <= wind < 6.0:
        return 80.0
    elif 13.0 <= wind <= 20.0:
        return 30.0
    else:
        return 0.0


def calculate_combined_score(tempScore, cloudScore, windScore, precip, day):
    # Combined Score Calculation
    combinedScore = (tempScore + windScore + cloudScore) / 3

    if precip >= 10 or day == 0:
        combinedScore = 0

    return combinedScore


def get_washing_recommendation(combinedScore):
    if combinedScore >= 80.0:
        return "excellent conditions for car washing."
    elif combinedScore >= 65.0:
        return "good conditions for car washing."
    elif combinedScore >= 50.0:
        return "fair conditions for car washing."
    else:
        return "poor conditions for car washing."
def get_color_class(washingRecommendation):
    if washingRecommendation == "excellent conditions for car washing.":
        return "excellent"
    elif washingRecommendation == "good conditions for car washing.":
        return "good"
    elif washingRecommendation == "fair conditions for car washing.":
        return "fair"
    else:
        return ""