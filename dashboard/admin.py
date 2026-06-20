from django.contrib import admin
from .models import Farm, Crop, WeatherData

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'variety', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'variety')

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'farmer', 'location', 'size', 'soil_type')
    list_filter = ('soil_type', 'location')
    search_fields = ('name', 'farmer__username', 'location')

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('region', 'temperature', 'humidity', 'rainfall', 'date_recorded')
    list_filter = ('region', 'date_recorded')
