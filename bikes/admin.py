from django.contrib import admin
from .models import Bike, Rental

# Register your models here.
admin.site.register(Bike)
admin.site.register(Rental)