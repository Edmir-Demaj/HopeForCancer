from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Category(models.Model):
    """
    This class Category defines the structure of Category
    model in our database and the methods.
    """
    category_name = models.CharField(
        max_length=50, unique=True, blank=False, null=False
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    """
    This class Post defines the structure of Post model
    in our database and the methods.
    """
    title = models.CharField(
        max_length=60, unique=True, blank=False, null=False,
        help_text=(
            'Please provide a descriptive title for your post. '
            'Maximum length is 60 characters.'
        )
    )
    slug = models.SlugField(max_length=60, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    describe_image = models.CharField(
        max_length=70, default='This is a default image.',
        help_text=(
            'Provide a short image description by removing the default text.'
        )
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_posts',
        help_text='Select a relevant Category that aligns with your story.'
    )
    content = models.TextField(
        help_text='Share your inspiring cancer story with us. '
                  "Your words can make a difference in someone's life."
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    comment_counter = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title + " - " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

# For ease of building this project the code below is kept same
# as blog walkthrough project in FST module, credits on Readme.md


class Comment(models.Model):
    """
    This class Comment defines the structure of Comment model
    in our database and the methods.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        To order the comments on the created_date field in the ascending order
        """

        ordering = ['created_date']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"
