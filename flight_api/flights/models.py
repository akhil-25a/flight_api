from django.db import models

# Create your models here.
from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model

class Flight(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stops = models.IntegerField()  # 0: non-stop, 1: 1 stop, etc.

    wifi_available = models.BooleanField(default=False)
    inflight_meal = models.BooleanField(default=False)

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_location} to {self.to_location} - {self.airline.name}"
