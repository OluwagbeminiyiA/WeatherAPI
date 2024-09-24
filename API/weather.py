import requests
from django.conf import settings


def get_weather_info(location: str, date1=None, date2=None):
    if not date1:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={settings.WEATHER_API_KEY}"
        responses = requests.get(url=url).json()
        date = responses['days'][0]['datetime']
        humidity = responses['days'][0]['humidity']
        snow = responses['days'][0]['snow']
        temp = f"{responses['days'][0]['temp']} °F"
        conditions = responses['days'][0]['conditions']
        description = responses['days'][0]['description']
        return {'date': date, 'conditions': conditions, 'description': description, 'temperature': temp, 'humidity': humidity, 'snow': snow}


# print(get_weather_info("lagos"))
