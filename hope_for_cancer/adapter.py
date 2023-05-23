from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

# this code was taken from Stack overflow, credits on README.md


class UsernameMaxAdapter(DefaultAccountAdapter):
    """
    code to add max length to username field when signup
    """
    def clean_username(self, username):
        if len(username) < 3:
            raise ValidationError(
                'Please enter a username with at least 3 characters!'
            )
        elif len(username) > 12:
            raise ValidationError(
                'Please enter a username with at most 12 characters!'
            )
        return DefaultAccountAdapter.clean_username(
            self, username
            )
