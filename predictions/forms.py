from django import forms
from .models import YieldPrediction
from accounts.forms import BootstrapFormMixin

class YieldPredictionForm(BootstrapFormMixin, forms.ModelForm):
    CROP_CHOICES = (
        ('Wheat', 'Wheat'),
        ('Corn', 'Corn'),
        ('Cotton', 'Cotton'),
        ('Rice', 'Rice'),
        ('Soybeans', 'Soybeans'),
    )
    
    crop_type = forms.ChoiceField(
        choices=CROP_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = YieldPrediction
        fields = ('farm_size', 'crop_type', 'rainfall', 'temperature')
        widgets = {
            'farm_size': forms.NumberInput(attrs={'placeholder': 'e.g. 5.2 (acres)', 'min': 0.1}),
            'rainfall': forms.NumberInput(attrs={'placeholder': 'e.g. 150.5 (mm)'}),
            'temperature': forms.NumberInput(attrs={'placeholder': 'e.g. 28.2 (°C)'}),
        }
