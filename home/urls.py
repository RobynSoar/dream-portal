from django.urls import path
from . import views

urlpatterns = [
    path('', views.dream_home, name='home')
]