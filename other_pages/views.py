from django.shortcuts import render


def index(request):
    """
    When this function is called it takes the request and return the
    response which will render home page or index.html
    """
    return render(request, 'other_pages/index.html')
