"""
Models for the Home app.
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Status default
STATUS = ((0, "Draft"), (1, "Published"))


# Post model
class Post(models.Model):
    """
    Represents a blog post with user-generated content.

    ``title``
        A unique title for the most (max 200 characters).
    ``slug``
        A unique slug used for URLs (max 200 characters).
    ``author``
        A foreign key linking the post to a :model:`auth.User`.
    ``dream_or_nightmare``
        A choice field indicating whether the post is a dream or a nightmare.
    ``reoccurring``
        A boolean indicating whether the dream or nightmare is reoccurring.
    ``content``
        The main text content of the post.
    ``created_on``
        A timestamp indicating when the post was created.
    ``updated_on``
        A timestamp indicating when the post was last updated.
    ``status``
        An integer defining if the post is a draft or published.
    ``excerpt``
        A short preview of the post's content.
    ``likes``
        A many-to-many relationship tracking users who liked the post.
    ``image``
        An optional image for the post, stored via Cloudinary.
    """
    DREAM_OR_NIGHTMARE_CHOICES = [
        ('dream', 'Dream'),
        ('nightmare', 'Nightmare'),
    ]

    REOCCURRING_CHOICES = [
        (True, 'Reoccurring'),
        (False, 'Not Reoccurring'),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    dream_or_nightmare = models.CharField(
        max_length=10,
        choices=DREAM_OR_NIGHTMARE_CHOICES,
        default='dream'
    )
    reoccurring = models.BooleanField(
        choices=REOCCURRING_CHOICES, default=False
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        'auth.User', related_name='liked_posts', blank=True
    )
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Orders by newest post first to oldest.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the post title.
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the totel like count.
        """
        return self.likes.count()


# Comment model
class Comment(models.Model):
    """
    Represents a comment on a blog post.

    ``post``
        A foreign key linking the comment to a :model:`home.Post`.
    ``author``
        A foreign key linking the comment to the :model:`auth.User`
        who authored it.
    ``body``
        The main text content of the comment.
    ``reported``
        A boolean indicating whether the comment has been reported.
    ``created_on``
        A timestamp indicating when the comment was created.
    ``edited``
        A boolean indicating whether the comment has been edited.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    body = models.TextField()
    reported = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    class Meta:
        """
        Ordered by oldest comment first to newest.
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns comment content, the author and on which post.
        """
        return f"Comment {self.body} by {self.author} on {self.post}"
