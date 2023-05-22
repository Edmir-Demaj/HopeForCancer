from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import *
from .forms import ContactForm


def contact(request):
    """
    When this view is called it takes the request and return the
    response which will render contact page, validate contact form on
    submittion and retreive faqs from databse to display in frontend.
    """
    faq = FAQ.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # validate form and if is valid save it in db and provide user
        # with success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, '<i class="fa-solid fa-triangle-exclamation"></i>\
                     Failed to send the message! Try again please '
            )
    else:
        form = ContactForm()
    context = {
      'form': form,
      'faq': faq
    }
    template = 'contact.html'
    return render(request, template, context)
