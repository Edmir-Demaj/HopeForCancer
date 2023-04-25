from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment


class BlogPage(generic.ListView):
    """
    This class uses generic views to render blog page and
    view latest posts in a list using Post model data.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog/blog.html'
    context_object_name = 'all_posts'


def postDetail(request, slug):
    """
    This function takes a request and get neccessary data needed
    to render single post in post_detail.html template
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('created_date')

    context = {
        "post": post,
        "comments": comments,
        "user": request.user,
    }
    return render(request, "blog/post_detail.html", context)
