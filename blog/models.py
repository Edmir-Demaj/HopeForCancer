from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This class Post defines the structure of Post model
    in our database.
    """
    title = models.CharField(
        max_length=200, unique=True, blank=False, null=False,
        help_text='Please provide a descriptive title for your post.'
    )
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    describe_image = models.CharField(
        max_length=100, default='A beautiful image from the post.'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_posts'
    )
    content = models.TextField(
        help_text="Share your inspiring cancer story with us. "
                  "Your words can make a difference in someone's life."
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.ImageField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    comment_counter = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title + " - " + str(self.author)

    def number_of_likes(self):
        return self.likes.count()
