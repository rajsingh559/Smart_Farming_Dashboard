from django.db import models
from django.conf import settings

class Recommendation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='recommendations'
    )
    nitrogen = models.FloatField(help_text="Nitrogen ratio in soil (N)")
    phosphorus = models.FloatField(help_text="Phosphorus ratio in soil (P)")
    potassium = models.FloatField(help_text="Potassium ratio in soil (K)")
    temperature = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity ratio in %")
    ph = models.FloatField(help_text="Soil pH value")
    rainfall = models.FloatField(help_text="Rainfall amount in mm")
    
    recommended_crop = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rec for {self.user.username}: {self.recommended_crop} ({self.created_at.date()})"
