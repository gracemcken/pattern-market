from django.urls import path
from .views import AddPattern, Patterns

# Url Patterns

urlpatterns = [
    path('', AddPattern.as_view(), name='add_pattern'),
    path('patterns/', Patterns.as_view(), name='patterns')
]
