from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports_view, name='reports'),
    path('crop/', views.crop_dashboard, name='crop_dashboard'),
    path('weather/', views.weather_dashboard, name='weather_dashboard'),
    path('yield/', views.yield_dashboard, name='yield_dashboard'),
    path('farmers/', views.farmer_dashboard, name='farmer_dashboard'),
]

