from django.shortcuts import render
from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    """
    This class uses generic views to render blog page and
    view latest posts in a list by 6 using Post model.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog.html'
    paginate_by = 6
