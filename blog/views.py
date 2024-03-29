from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.utils.html import format_html
from django.http import HttpResponseRedirect, HttpResponseForbidden
from datetime import datetime
from django.core.validators import MaxLengthValidator
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
    liked = False
    # check if user request is from authenticated user to change the
    # icon of a liked/disliked post
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            liked = True
    comments = (Comment.objects
                .filter(post=post)
                .filter(approved=True)
                .order_by('created_date'))
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
        'liked': liked,
        'comment_form': CommentForm(),
    }
    return render(request, 'blog/post_detail.html', context)


class CreatePost(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    Create a blog post only when user is logged in, if is not loggedin will
    be redirected to the login page. Provide message to user.
    """
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/create_post.html'
    success_message = (
        'Post added successfully! Awaiting approval from Admin.'
    )

    def get_success_url(self):
        """
        Set the reverse url for the successful addition
        of the post to the database, reverse to blog_page
        """
        return reverse('blog_page')

    def form_valid(self, form):
        """
        This function sets the author field as user when form is submitted
        and if slug doesn't exist creats a unique slug from its title
        """
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


@login_required()
def update_post(request, slug):
    """
    Users can update their blog post that they have created,
    requires user to be loggedin and provide message to user.
    """
    post = get_object_or_404(Post, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        # If the current user is not the author, raise a 403 Forbidden error.
        return HttpResponseForbidden(
            "You don't have permission to edit this post!"
            " Please return back and edit only your posts."
        )

    if request.method == 'POST':
        form = UpdatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.status = 1
            form.save()
            messages.success(request, 'Your post updated successfully!')
            return redirect(reverse(
                'post_detail', kwargs={'slug': post.slug}
                ))
        else:
            messages.error(request, 'Failed to update the post.')
    else:
        form = UpdatePostForm(instance=post)

    context = {'update_form': form, 'post': post}
    return render(request, 'blog/update_post.html', context)


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    """
    View to allow users to delete a post and provide a message.
    """
    model = Post
    template_name = 'blog/delete_post.html'

    def delete(self, request, *args, **kwargs):
        # Get the post to be deleted
        post = self.get_object()

        # Check if the current user is the author of the post
        if post.author != self.request.user:
            # If the current user is not the author, raise a 403 error
            return HttpResponseForbidden(
                "You don't have permission to delete this post!"
            )
        messages.success(request, 'Post deleted successfully.')
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Reverse Url after post is deleted
        """
        slug = self.kwargs.get('slug')
        return reverse('blog_page')


class PostLike(LoginRequiredMixin, View):
    """
    View to make possible for users to like a post displaying a message.
    Has url to redirect as well.
    """
    def post(self, request, slug, *args, **kwargs):
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
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required()
def add_comment(request, post_id):
    """
    In this view we get the post where the comment is related to and save the
    comment in DB. Before saving we validate the form.Provide message depending
    on status of validation and increase number of comments.
    """
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(
            request, 'Comment added successfully! Awaiting approval from Admin'
        )
        return redirect(reverse('post_detail', args=(post.slug,)))
    else:
        comment_form = CommentForm()
        messages.error(
            request, '<i class="fa-solid fa-triangle-exclamation"></i>\
                    Comment failed to submit! Try again please '
        )
    return redirect(reverse('post_detail', args=(post.slug,)))


class EditComment(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    View to edit a comment and provide a message if update is successfull
    """
    model = Comment
    template_name = 'blog/edit_comment.html'
    form_class = CommentForm
    success_message = 'Your comment updated successfully!'

    def get_success_url(self):
        """
        Reverse Url after comment is updated
        """
        comment = self.get_object()
        post = comment.post
        return reverse('post_detail', args=[post.slug])


@login_required()
def delete_comment(request, comment_id):
    """
    Delete comment and provide a message to user
    """
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    name = comment.name
    # decrease comment counter when comment is deleted
    if comment.approved:
        post.comment_counter -= 1
        post.save()
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
