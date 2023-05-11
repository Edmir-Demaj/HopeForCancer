from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from .models import Value


def index(request):
    """
    When this function is called it takes the request and return the
    response which will render home page or index.html as well as
    show the latest 3 blog posts.
    """
    latest_posts = Post.objects.filter(status=1).order_by('-created_date')[:3]
    for post in latest_posts:
        post.num_comments = Comment.objects.filter(post=post).count()
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


def info_page(request):
    """
    When this function is called it takes the request and return the
    response which will render cancer information page.
    """
    template = 'other_pages/info.html'
    return render(request, template)


def my_view(request):
    return render(request, '404.html')
