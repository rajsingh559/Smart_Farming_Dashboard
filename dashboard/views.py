from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Farm, WeatherData
from feedback.models import Rating

User = get_user_model()

def landing_view(request):
    """Public landing page containing key features of the Smart Farming Dashboard."""
    # Fetch some highlights for landing stats
    context = {
        'total_farmers': User.objects.filter(role='farmer').count(),
        'total_farms': Farm.objects.count()
    }
    return render(request, 'dashboard/landing.html', context)

@login_required
def dashboard_view(request):
    """Secure home dashboard rendering agricultural stats, KPI cards, and visual charts."""
    # Database stats
    total_farmers = User.objects.filter(role='farmer').count()
    active_farms = Farm.objects.count()
    
    # Simple calculation for average rating satisfaction
    ratings = Rating.objects.all()
    avg_rating = sum(r.score for r in ratings) / ratings.count() if ratings.exists() else 4.8
    
    # Mock data for dashboard cards
    crop_yield_index = "88.4 / 100"
    avg_rainfall = "112.5 mm"
    weather_status = "Sunny, 24°C"

    # Context for charts
    context = {
        'total_farmers': total_farmers,
        'active_farms': active_farms,
        'avg_rating': f"{avg_rating:.1f}",
        'crop_yield_index': crop_yield_index,
        'avg_rainfall': avg_rainfall,
        'weather_status': weather_status,
        # Mock weather & distribution datasets for Chart.js
        'crop_labels': ['Wheat', 'Corn', 'Cotton', 'Rice', 'Soybeans'],
        'crop_data': [35, 25, 15, 15, 10],
        'monthly_rainfall_labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'monthly_rainfall_data': [45, 60, 95, 120, 80, 50],
        'seasonal_labels': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'seasonal_yield_data': [75, 90, 85, 40]
    }
    return render(request, 'dashboard/dashboard.html', context)
