"""
This module contains the views for the Home application.
It includes the logic to render templates and handle requests.
"""

from django.shortcuts import render, get_object_or_404
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
    template_name = "home/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`home.Post`.

    **Context**

    ``post``
        An instance of :model:`home.Post`.

    **Template:**

    :template:`home/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "home/post_detail.html",
        {"post": post},
    )