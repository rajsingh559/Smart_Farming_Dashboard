from django.contrib import admin
from .models import YieldPrediction

@admin.register(YieldPrediction)
class YieldPredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'crop_type', 'farm_size', 'predicted_yield', 'created_at')
    list_filter = ('crop_type', 'created_at')
    search_fields = ('user__username', 'crop_type')
