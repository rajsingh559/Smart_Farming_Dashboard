from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_yield_view, name='predict_yield'),
]
