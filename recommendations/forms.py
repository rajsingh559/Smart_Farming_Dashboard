from django import forms
from .models import Recommendation
from accounts.forms import BootstrapFormMixin

class CropRecommendationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall')
        widgets = {
            'nitrogen': forms.NumberInput(attrs={'placeholder': 'e.g. 50 (ppm)', 'min': 0, 'max': 140}),
            'phosphorus': forms.NumberInput(attrs={'placeholder': 'e.g. 40 (ppm)', 'min': 0, 'max': 140}),
            'potassium': forms.NumberInput(attrs={'placeholder': 'e.g. 40 (ppm)', 'min': 0, 'max': 210}),
            'temperature': forms.NumberInput(attrs={'placeholder': 'e.g. 25.4 (°C)', 'step': 0.1}),
            'humidity': forms.NumberInput(attrs={'placeholder': 'e.g. 60.5 (%)', 'step': 0.1}),
            'ph': forms.NumberInput(attrs={'placeholder': 'e.g. 6.5', 'step': 0.1, 'min': 0, 'max': 14}),
            'rainfall': forms.NumberInput(attrs={'placeholder': 'e.g. 100.2 (mm)', 'step': 0.1}),
        }
