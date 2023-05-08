from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .models import Value


def index(request):
    """
    When this function is called it takes the request and return the
    response which will render home page or index.html as well as
    show the latest 3 blog posts.
    """
    latest_posts = Post.objects.order_by('-created_date')[:3]
    context = {'latest_posts': latest_posts}
    template = 'other_pages/index.html'
    return render(request, template, context)


def about_page(request):
    """
    When this function is called it takes the request and return the
    response which will render about page.
    """
    values = Value.objects.all()
    template = 'other_pages/about.html'
    context = {
        'values': values,
    }
    return render(request, template, context)
