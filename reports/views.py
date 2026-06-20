from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def reports_view(request):
    """Redirect to the default Crop Analysis report."""
    return redirect('crop_dashboard')

@login_required
def crop_dashboard(request):
    """Crop Analysis Dashboard showing crop production trends."""
    context = {
        'title': 'Crop Analysis Dashboard',
        'description': 'Displays crop production trends, crop distribution, seasonal performance, and region-wise agricultural insights.',
        'dashboard_url': 'https://public.tableau.com/views/Smart_Farming_DashboardCrop_Analysis/Dashboard1?:showVizHome=no',
    }
    return render(request, 'reports/crop.html', context)

@login_required
def weather_dashboard(request):
    """Weather Analytics Dashboard showing weather trends."""
    context = {
        'title': 'Weather Analytics Dashboard',
        'description': 'Displays rainfall analysis, temperature patterns, humidity trends, and seasonal weather statistics.',
        'dashboard_url': 'https://public.tableau.com/views/Smart_Farming_Dashboard/Dashboard2?:showVizHome=no',
    }
    return render(request, 'reports/weather.html', context)

@login_required
def yield_dashboard(request):
    """Yield Prediction Dashboard showing yield metrics."""
    context = {
        'title': 'Yield Prediction Dashboard',
        'description': 'Displays predicted crop yield metrics, production forecasts, and analytical insights generated from machine learning models.',
        'dashboard_url': 'https://public.tableau.com/views/Smart_Farming_DashboardYield_Prediction/Dashboard3?:showVizHome=no',
    }
    return render(request, 'reports/yield.html', context)

@login_required
def farmer_dashboard(request):
    """Farmer Statistics Dashboard showing farmer insights."""
    context = {
        'title': 'Farmer Statistics Dashboard',
        'description': 'Displays farmer registrations, farm distribution, crop preferences, and agricultural demographic insights.',
        'dashboard_url': 'https://public.tableau.com/views/Smart_Farming_DashboardFarmer_Statistics/Dashboard4?:showVizHome=no',
    }
    return render(request, 'reports/farmers.html', context)

