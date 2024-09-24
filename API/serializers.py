from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=200)
    date1 = serializers.DateField(default=None)
    date2 = serializers.DateField(default=None)