from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Status default
STATUS = ((0, "Draft"), (1, "Published"))


# Post model
class Post(models.Model):
    DREAM_OR_NIGHTMARE_CHOICES = [
        ('dream', 'Dream'),
        ('nightmare', 'Nightmare'),
    ]

    REOCCURRING_CHOICES = [
        (True, 'Reoccuring'),
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
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# Comment model
class Comment(models.Model):
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
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author} on {self.post}"
