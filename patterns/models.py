from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Pattern Choice Fields

PATTERN_TYPE = (
    ('crossstitch', 'CrossStitch'),
    ('blackwork', 'Blackwork'),
    ('embroidery', 'Embroidery')
)

# Create your models here.


class Pattern(models.Model):
    """
    Model to create and manage pattern posts.
    """
    user = models.ForeignKey(
        User, related_name='pattern_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    supplies = RichTextField(max_length=10000, null=False, blank=False)
    pattern_guide = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='patterns/', force_format='WEBP', null=False, blank=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    pattern_type = models.CharField(
        max_length=50, choices=PATTERN_TYPE, default='mixed')
    colors = models.IntegerField()
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return str(self.title)
