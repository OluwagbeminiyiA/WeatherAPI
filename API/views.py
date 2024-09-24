from django.utils.decorators import method_decorator
from django.views.decorators import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LocationSerializer
from .weather import get_weather_info
from rest_framework import status


# Create your views here.

class WeatherAPI(APIView):

    @method_decorator(cache.cache_page(60*60*2))
    def get(self, request):
        print(request.query_params)
        serializer = LocationSerializer(data=request.query_params)
        if serializer.is_valid():
            response = get_weather_info(serializer.validated_data['location'])
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
