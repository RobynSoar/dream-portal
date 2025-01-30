"""
Views for the Home app.

Functionality to display posts, handle comments, and manage user interactions.
"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


def dream_home(request):
    """
    Renders the 'base.html' template for the Home application.
    """
    return render(request, 'base.html')


class PostList(generic.ListView):
    """
    Display a paginated list of published :model:`home.Post` instances.

    **Context**

    ``queryset``
        A queryset containing published posts (status=1),
        Ordered by creation date (newest first).
    ``template_name``
        The template used to render the post list.
    ``paginate_by``
        The number of posts displayed per page.

    **Template:**

    :template:`home/index.html`
    """
    queryset = Post.objects.order_by("-created_on").filter(status=1)
    template_name = "home/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`home.Post`.

    **Context**

    ``post``
        An instance of :model:`home.Post`.
    ``comments``
        All comments related to the post.
    ``comment_count``
        A count of comments related to the post.
    ``comment_form``
        An instance of :form:`home.CommentForm`.

    **Template:**

    :template:`home/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()

    # If user submits a comment
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    comment_form = CommentForm()

    return render(
        request,
        "home/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit individual comments

    **Context**

    ``post``
        An instance of :model:`home.Post`.
    ``comments``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`home.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.edited = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete individual comments

    **Context**

    ``post``
        An instance of :model:`home.Post`.
    ``comments``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    # Returns user to previous page, to comments section after comment deletion
    return HttpResponseRedirect(
        reverse('post_detail', args=[slug]) + "#comments"
    )
