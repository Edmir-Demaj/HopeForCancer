from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Contact(models.Model):
    """
    This is the contact model in DB.
    """
    name = models.CharField(
        max_length=20, blank=False, null=False,
        validators=[
            MinLengthValidator(
                3, message='Name must have at least 3 characters.'
            ),
            MaxLengthValidator(20, message='Name cannot exceed 20 characters.')
        ])
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                10, message='Subject must have at least 10 characters.'
            ),
            MaxLengthValidator(
                100, message='Subject cannot exceed 100 characters.'
            )],)
    content = models.TextField(
        blank=False, null=False, validators=[MinLengthValidator(
            10, message='Content must have at least 10 characters.')],)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """
    This is the FAQ model in DB.
    """
    title = models.CharField(max_length=150, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'FAQs'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.title
