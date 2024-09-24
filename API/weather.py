import requests
from django.conf import settings


def get_weather_info(location: str, date1=None, date2=None):
    if not date1:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={settings.WEATHER_API_KEY}"
        responses = requests.get(url=url).json()
        date = responses['days'][0]['datetime']
        conditions = responses['days'][0]['conditions']
        description = responses['days'][0]['description']
        return {'date': date, 'conditions': conditions, 'description': description}


# print(get_weather_info("lagos"))
