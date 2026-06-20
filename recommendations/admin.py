from django.contrib import admin
from .models import Recommendation

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommended_crop', 'nitrogen', 'phosphorus', 'potassium', 'ph', 'created_at')
    list_filter = ('recommended_crop', 'created_at')
    search_fields = ('user__username', 'recommended_crop')
