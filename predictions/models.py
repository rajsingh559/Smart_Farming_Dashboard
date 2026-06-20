from django.db import models
from django.conf import settings

class YieldPrediction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='yield_predictions'
    )
    farm_size = models.FloatField(help_text="Farm size in acres")
    crop_type = models.CharField(max_length=100)
    rainfall = models.FloatField(help_text="Expected rainfall in mm")
    temperature = models.FloatField(help_text="Expected temperature in Celsius")
    predicted_yield = models.FloatField(help_text="Predicted yield in tons")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.user.username}: {self.predicted_yield} tons ({self.created_at.date()})"
