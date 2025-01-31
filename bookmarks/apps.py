"""
Configuration for the 'Bookmarks' app
"""
from django.apps import AppConfig


class BookmarksConfig(AppConfig):
    """
    Configuration for the 'bookmarks' app.

    ``default_auto_field``
        Defines the default auto field type and the name of the app.
    ``name``
        Name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookmarks'
