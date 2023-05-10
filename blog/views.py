from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from .models import *
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
    paginate_by = 5


def postDetail(request, slug):
    """
    This function takes a request and get neccessary data needed
    to render single post in post_detail.html template.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = Comment.objects.filter(post=post).order_by('created_date')

    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
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
    success_message = (
        "Post added successfully! Awaiting approval from Admin."
    )

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


@login_required()
def update_post(request, slug):
    """
    Users can update their blog post that they have created
    """
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.status = 1
            form.save()
            messages.success(request, "Your post updated successfully!")
            return redirect(reverse(
                "post_detail", kwargs={'slug': post.slug}
                ))
        else:
            messages.error(request, "Failed to update the post.")
    else:
        form = UpdatePostForm(instance=post)

    context = {"update_form": form, "post": post}
    return render(request, 'blog/update_post.html', context)


class DeletePost(generic.DeleteView):
    """
    View to allow users to delete a post
    """
    model = Post
    template_name = "blog/delete_post.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Reverse Url after post is deleted
        """
        slug = self.kwargs.get('slug')
        return reverse("blog_page")


class PostLike(generic.View):
    """
    View to make possible for users to like a post
    """
    def post(self, request, slug, *args):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            message = format_html(
                'You disliked this post. '
                '<i class="fa-regular fa-face-frown"></i>'
            )
        else:
            post.likes.add(request.user)
            message = format_html(
                'You liked this post. '
                '<i class="fa-regular fa-face-smile"></i>'
            )
        messages.success(request, message)
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))
