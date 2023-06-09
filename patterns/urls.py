from django.urls import path
from .views import AddPattern, Patterns, PatternDetail, DeletePattern, EditPattern

# Url Patterns

urlpatterns = [
    path("add/", AddPattern.as_view(), name="add_pattern"),
    path("", Patterns.as_view(), name="patterns"),
    path("<slug:pk>/", PatternDetail.as_view(), name="pattern_detail"),
    path("delete/<slug:pk>/", DeletePattern.as_view(), name="delete_pattern"),
    path("edit/<slug:pk>/", EditPattern.as_view(), name="edit_pattern"),
]
