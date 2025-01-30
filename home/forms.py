"""
Form config for blog posts and comments.
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments on blog posts.
    """
    class Meta:
        """
        **Context**

        ``model``
            :model:`home.Comment`.
        ``body``
            Text content of the comment.
        """
        model = Comment
        fields = ('body',)
