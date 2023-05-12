from django.shortcuts import render
from .models import *


def contact(request):
    """
    When this function is called it takes the request and return the
    response which will rendercontact page.
    """
    template = 'contact.html'
    return render(request, template)
