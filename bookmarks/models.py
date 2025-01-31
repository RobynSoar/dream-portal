"""
Models for the Bookmarks app
"""

from django.db import models


class Bookmark(models.Model):
    """
    User can bookmark posts to go back to later
    Each bookmark links a user to a specific post,
    allowing them to save posts
    for easy access later.

    ``user``
        Foreign key - User who bookmarked the post.
    ``post``
        Foreign key - The post that was bookmarked
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(
        'home.Post', on_delete=models.CASCADE, related_name='bookmarks'
    )

    class Meta:
        """
        Ensures user cannot bookmark the same post multiple times
        """
        unique_together = ['user', 'post']

    def __str__(self):
        """
        Returns title of bookmarked post and author to user
        """
        return f"{self.post.title} by {self.post.author}"
