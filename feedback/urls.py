from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list_view, name='feedback_list'),
]
