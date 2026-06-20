from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CropRecommendationForm
from .models import Recommendation

@login_required
def recommend_crop_view(request):
    """View to handle soil input submission, recommend crop, and list prior history."""
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            
            # Simple rules-based fallback model for Phase 1 (replaced by ML model in Phase 4)
            # Just to prove database persistence and workflow stability
            ph = recommendation.ph
            temp = recommendation.temperature
            if ph < 5.5:
                crop = "Rice"
            elif temp > 30:
                crop = "Cotton"
            elif recommendation.nitrogen > 80:
                crop = "Maize"
            else:
                crop = "Wheat"
                
            recommendation.recommended_crop = crop
            recommendation.save()
            messages.success(request, f"Crop Recommendation Generated: {crop}!")
            return redirect('recommend_crop')
    else:
        form = CropRecommendationForm()
        
    # Get user history
    history = Recommendation.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'form': form,
        'history': history,
    }
    return render(request, 'recommendations/recommend.html', context)
