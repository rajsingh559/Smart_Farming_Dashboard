from django.db import models
from django.conf import settings

class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    variety = models.CharField(max_length=100, blank=True, help_text="e.g. Basmati, Hybrid")
    category = models.CharField(max_length=50, blank=True, help_text="e.g. Cereal, Legume, Vegetable")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Farm(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size = models.FloatField(help_text="Size in acres")
    soil_type = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.username}"

class WeatherData(models.Model):
    region = models.CharField(max_length=100)
    temperature = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity percentage")
    rainfall = models.FloatField(help_text="Rainfall in mm")
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Weather at {self.region} on {self.date_recorded}"
