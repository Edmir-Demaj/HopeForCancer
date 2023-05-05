from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from .models import Post, Comment
from .forms import *


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
    # success_message = ("Great job! You have successfully added a new post "
    #                    "and it is now pending approval.")

    def get_success_url(self):
        """
        Set the reverse url for the successful addition
        of the post to the database, reverse to blog_page
        """
        return reverse("blog_page")

    def form_valid(self, form):
        """
        This function sets the author field as user when form is submitted
        and if slug doesnt exist creats a unique slug from its title
        """
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, generic.CreateView):

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        update_form = UpdatePostForm(data=request.Post)
        template_name = "blog/update_post.html"
        context = {
            "update_form": update_form,
            "post": post
        }
        if request.user.id == post.author.id:

            if update_form.is_valid():
                update_form.save(commit=False)
                update_form.instance.author = request.user
                update_form.instance.slug = slugify(post.title)
                update_form.instance.status = 1
                update_form.save()
            else:
                messages.error(request, "Failed to update the post.")
            return render(request, template_name, context)
        else:
            messages.error(request, "Sorry, This is not your post.")
