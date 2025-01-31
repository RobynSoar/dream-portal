from django.urls import path
from . import views

urlpatterns = [
    path('add/<slug:slug>/', views.add_bookmark, name='add_bookmark'),
    path('my/', views.my_bookmarks, name='my_bookmarks'),
]