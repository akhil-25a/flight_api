from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Flight, Airline, Aircraft

admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Aircraft)
