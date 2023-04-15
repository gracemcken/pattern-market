from django.urls import path
from .views import AddPattern, Patterns, PatternDetail, DeletePattern

# Url Patterns

urlpatterns = [
    path("", AddPattern.as_view(), name="add_pattern"),
    path("patterns/", Patterns.as_view(), name="patterns"),
    path("<slug:pk>/", PatternDetail.as_view(), name="pattern_detail"),
    path("delete/<slug:pk>/", DeletePattern.as_view(), name="delete_pattern"),
]
