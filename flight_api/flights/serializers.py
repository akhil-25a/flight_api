from rest_framework import serializers
from .models import Flight, Airline, Aircraft

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    aircraft = AircraftSerializer()

    class Meta:
        model = Flight
        fields = '__all__'
