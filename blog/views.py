from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CreatePostForm


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
    to render single post in post_detail.html template.
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


class CreatePost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    Create a blog post only when user is logged in, if is not loggedin will
    be redirected to the login page.
    """
    model = Post
    form_class = CreatePostForm
    template_name = "blog/create_post.html"
    success_message = ("Great job! You have successfully added a new post "
                       "and it is now pending approval.")

    # def get_success_url(self):
    #     """
    #     Set the reverse url for the successful addition
    #     of the post to the database
    #     """
    #     return reverse("blog_page")

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.slug = slugify(form.instance.title)
    #     return super().form_valid(form)
