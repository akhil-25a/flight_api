from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Flight
from .serializers import FlightSerializer
from django.db.models import Q
from datetime import time

class FlightSearchAPIView(APIView):
    def get(self, request):
        flights = Flight.objects.all()

        # Location
        from_location = request.GET.get('from')
        to_location = request.GET.get('to')
        if from_location:
            flights = flights.filter(from_location__iexact=from_location)
        if to_location:
            flights = flights.filter(to_location__iexact=to_location)

        # Price
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if min_price and max_price:
            flights = flights.filter(price__range=(min_price, max_price))

        # Stops
        stops = request.GET.get('stops')
        if stops is not None:
            flights = flights.filter(stops=int(stops))

        # Departure time window
        dep_window = request.GET.get('departure_window')
        if dep_window:
            time_ranges = {
                'morning': (time(5, 0), time(11, 59)),
                'afternoon': (time(12, 0), time(16, 59)),
                'evening': (time(17, 0), time(20, 59)),
                'night': (time(21, 0), time(4, 59)),
            }
            start, end = time_ranges.get(dep_window.lower(), (None, None))
            if start and end:
                if start < end:
                    flights = flights.filter(departure_time__time__range=(start, end))
                else:  # Night (e.g. 21:00 to 04:59)
                    flights = flights.filter(Q(departure_time__time__gte=start) | Q(departure_time__time__lte=end))

        # WiFi
        wifi = request.GET.get('wifi')
        if wifi == "true":
            flights = flights.filter(wifi_available=True)

        # Meals
        meals = request.GET.get('meals')
        if meals == "true":
            flights = flights.filter(inflight_meal=True)

        # Aircraft model
        aircraft = request.GET.get('aircraft')
        if aircraft:
            flights = flights.filter(aircraft__model__iexact=aircraft)

        # Airline
        airline = request.GET.get('airline')
        if airline:
            flights = flights.filter(airline__name__icontains=airline)

        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
