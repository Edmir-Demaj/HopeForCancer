from django.db import models


class Contact(models.Model):
    """
    This is the contact model in DB.
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=100)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """
    This is the FAQ model in DB.
    """
    title = models.CharField(max_length=150, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
