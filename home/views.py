"""
This module contains the views for the Home application.
It includes the logic to render templates and handle requests.
"""

from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
def dream_home(request):
    """
    Renders the 'base.html' template for the Home application.
    """
    return render(request, 'base.html')


class PostList(generic.ListView):
    queryset = Post.objects.order_by("-created_on").filter(status=1)
    template_name = "post_list.html"
