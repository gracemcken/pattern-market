from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Pattern


class PatternForm(forms.ModelForm):
    """Form to create pattern"""
    class Meta:
        model = Pattern
        fields = ['title', 'description', 'supplies', 'pattern_guide',
                  'image', 'image_alt', 'pattern_type', 'colors']
        supplies = forms.IntegerField(widget=RichTextWidget())
        pattern_guide = forms.CharField(widget=RichTextWidget())

        widget = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {
            'title': 'Pattern Title',
            'description': 'Description',
            'supplies': 'Pattern Supplies',
            'image': 'Pattern Image',
            'image_alt': 'Describe Image',
            'pattern_type': 'Pattern Type',
            'colors': 'Colors'
        }
