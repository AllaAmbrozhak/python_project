from django.views.generic import TemplateView
from django.shortcuts import render
import requests


class YourGeolocationView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {
            'latitude': self.latitude(),
            'longitude': self.longitude()
        })

    def latitude(self):
        response = requests.get('http://freegeoip.net/json')
        return response.json()['latitude']

    def longitude(self):
        response = requests.get('http://freegeoip.net/json')
        return response.json()['longitude']


class YourForecastView(TemplateView):

    def get(self, request, *args, **kwargs):
        geo = YourGeolocationView()
        parameters = {"lat": geo.latitude(), "lon": geo.longitude(), "appid": "b6907d289e10d714a6e88b30761fae22"}
        response = requests.get("http://samples.openweathermap.org/data/2.5/weather", params=parameters)
        weather = response.json()
        return render(request, 'weather.html', {
            'temperature': weather['main']['temp'],
            'pressure': weather['main']['pressure'],
            'humidity': weather['main']['humidity'],
        })
