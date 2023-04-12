from django.urls import path
from .views import AddPattern

# Url Patterns

urlpatterns = [
    path('', AddPattern.as_view(), name='add_pattern'),
]
