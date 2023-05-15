from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Value(models.Model):
    """
    Value model used in about page to render images and text
    """
    featured_image = CloudinaryField('image')
    image_description = models.CharField(
        max_length=100, blank=True, null=True,
        help_text=(
            'Please provide a description for the image.'
        )
    )
    title = models.CharField(
        max_length=100, unique=True, blank=False, null=False,
        help_text=(
            'Please provide a descriptive title for your post.'
        )
    )
    content = models.TextField(
      help_text='Please provide your Website Values content on this field.'
    )

    def __str__(self):
        return self.title
