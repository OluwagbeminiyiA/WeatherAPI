from django.urls import path
from . import views

urlpatterns = [
    path('', views.WeatherAPI.as_view(), name='weather')
]
