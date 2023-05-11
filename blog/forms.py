from .models import Post, Comment
from django import forms
from django.forms import widgets


class CreatePostForm(forms.ModelForm):
    """
    Form for users to create a new post.
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'describe_image',
            'category',
            'content',
        )


class UpdatePostForm(forms.ModelForm):
    """
    Form for users to update a post.
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'describe_image',
            'category',
            'content',
        )


class CommentForm(forms.ModelForm):
    """
    Form for users to comment a post.
    """
    body = forms.CharField(
        label='Leave a comment:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write your comment here',
                }
            )
    )

    class Meta:
        model = Comment
        fields = ('body',)
