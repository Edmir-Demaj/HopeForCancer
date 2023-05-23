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
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email',
                }
            )
    )
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a subject for your message',
                }
            )
    )

    content = forms.CharField(
        label='Message',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter your message',
                'rows': 8
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


def clean_name(self):
    # Remove all whitespace characters from name field
    name = self.cleaned_data.get('name')
    if name:
        name = name.replace(' ', '')
    return name


def clean_email(self):
    # Remove all whitespace characters from email field
    email = self.cleaned_data.get('email')
    if email:
        email = email.replace(' ', '')
    return email


def clean_subject(self):
    # Remove all whitespace characters from subject field
    subject = self.cleaned_data.get('subject')
    if subject:
        subject = subject.replace(' ', '')
    return subject
