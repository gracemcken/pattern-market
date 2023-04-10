from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

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
