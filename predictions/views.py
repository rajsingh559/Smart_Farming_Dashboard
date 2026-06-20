from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import YieldPredictionForm
from .models import YieldPrediction

@login_required
def predict_yield_view(request):
    """View to handle yield prediction submission, run regression logic, and show logs."""
    if request.method == 'POST':
        form = YieldPredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.user = request.user
            
            # Simple rule-based yield formula for Phase 1 (replaced by ML model in Phase 4)
            # e.g., Base yield per acre * farm size, adjusted by temperature
            base_yields = {
                'Wheat': 2.5,
                'Corn': 3.8,
                'Cotton': 1.8,
                'Rice': 3.0,
                'Soybeans': 2.2
            }
            crop = prediction.crop_type
            factor = base_yields.get(crop, 2.0)
            
            # Adjust based on temp (penalize if too high or low)
            temp = prediction.temperature
            temp_mult = 1.0
            if temp > 35 or temp < 15:
                temp_mult = 0.7
            
            predicted = factor * prediction.farm_size * temp_mult
            prediction.predicted_yield = round(predicted, 2)
            prediction.save()
            
            messages.success(request, f"Yield prediction generated: {prediction.predicted_yield} tons!")
            return redirect('predict_yield')
    else:
        form = YieldPredictionForm()
        
    history = YieldPrediction.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'form': form,
        'history': history,
    }
    return render(request, 'predictions/predict.html', context)
