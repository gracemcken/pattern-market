from django.contrib import admin
from .models import Pattern

# Register your models here.


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pattern_type',
        'colors',
        'image',
        'pattern_guide'
    )

    list_filter = ('pattern_type')
