from .models import Post
from django import forms


class CreatePostForm(forms.ModelForm):
    """
    Form for users to create a new post.
    """
    class Meta:
        model = Post
        fields = (
            "title",
            "featured_image",
            "describe_image",
            "category",
            "content",
        )


class UpdatePostForm(forms.ModelForm):
    """
    Form for users to update a post.
    """
    class Meta:
        model = Post
        fields = (
            "title",
            "featured_image",
            "describe_image",
            "category",
            "content",
        )
