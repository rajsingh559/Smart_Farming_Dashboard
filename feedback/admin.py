from django.contrib import admin
from .models import Feedback, Rating

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'feedback_text', 'created_at')
    search_fields = ('user__username', 'feedback_text')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'created_at')
    list_filter = ('score', 'created_at')
