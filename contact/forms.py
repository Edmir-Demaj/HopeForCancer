from .models import Contact
from django import forms
from django.forms import widgets


class ContactForm(forms.ModelForm):
    """
    Form for users to submit a contact form to admin.
    """
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your name',
                }
            )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your email',
                }
            )
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please provide a subject for your message',
                }
            )
    )

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'content',
        )
