from django.db import models


class Contact(models.Model):
    """
    This is the contact model in DB.
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
