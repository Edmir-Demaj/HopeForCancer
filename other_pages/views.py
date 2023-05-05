from django.shortcuts import render
from blog.models import Post


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
