"""
This module contains the views for the Home application.
It includes the logic to render templates and handle requests.
"""

from django.shortcuts import render


# Create your views here.
def dream_home(request):
    """
    Renders the 'base.html' template for the Home application.
    """
    return render(request, 'base.html')
