"""
Configuration for the apps.
"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration for the 'home' app.

    ``default_auto_field``
        Defines the default auto field type and the name of the app.
    ``name``
        Name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
