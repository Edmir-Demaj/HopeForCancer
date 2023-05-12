from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import ContactForm


def contact(request):
    """
    When this function is called it takes the request and return the
    response which will rendercontact page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
        else:
            messages.error(
                request, '<i class="fa-solid fa-triangle-exclamation"></i>\
                     Failed to send the message! Try again please '
            )
    else:
        form = ContactForm()
    context = {
      'form': form
    }
    template = 'contact.html'
    return render(request, template, context)
