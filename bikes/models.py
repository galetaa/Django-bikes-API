from django.db import models
from django.conf import settings


class Bike(models.Model):
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)


class Rental(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
