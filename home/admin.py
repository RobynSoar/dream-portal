"""
Admin interface config for managing 'Post' and 'Comment' models.
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Custom admin interface for managing a post in the Django Admin Panel.

    ``list_display``
        Displays title, slug, status, and creating date.
    ``search_fields``
        Enables search functionality for title and content fields.
    ``list_filters``
        Filters by status and creation date.
    ``prepopulated_fields``
        Automatically fills in the slug field based on the title.
    ``summernote_fields``
        Uses Summernote for rich text editing off the content field.
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
