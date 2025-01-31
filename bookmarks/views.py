"""
Views for the Bookmarks app.

Functionality to bookmark posts, and display previously
bookmarked posts to the user.
"""

from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from home.models import Post
from .models import Bookmark


def add_bookmark(request, slug):
    """
    Add a bookmark for a specific post if the user is authenticated.

    If the user is authenticated, the post will be bookmarked.

    ``post``
        An instance of :model:`blog.Post`.
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=slug, status=1)

        # Makes sure the user has not already bookmarked the post
        if not Bookmark.objects.filter(user=request.user, post=post).exists():
            Bookmark.objects.create(user=request.user, post=post)
            messages.add_message(
                request, messages.SUCCESS, 'Post bookmarked successfully!'
            )
        else:
            messages.add_message(
                request, messages.INFO,
                'You have already bookmarked this post.'
            )

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        messages.add_message(
            request, messages.ERROR,
            'You need to be logged in to bookmark posts.'
        )


def my_bookmarks(request):
    """
    Display a list of bookmarks for the authenticated user.

    If the user is authenticated, their bookmarked posts will be shown.
    """
    if request.user.is_authenticated:
        # Retrieve all bookmarks for the logged-in user
        bookmarks = Bookmark.objects.filter(user=request.user)

        # Fetch the posts related to bookmarks
        bookmarked_posts = [bookmark.post for bookmark in bookmarks]

        return render(
            request,
            'bookmarks/my_bookmarks.html',
            {
                'bookmarked_posts': bookmarked_posts
            }
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You need to be logged in to view your bookmarks.'
        )
