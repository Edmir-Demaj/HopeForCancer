from django.test import TestCase, Client
from django.urls import reverse, resolve
from blog.models import *
from blog.views import *


class BlogAppTestViews(TestCase):
    """
    This class test all BlogPage attributes
    """
    def test_blog_page_view(self):
        url = reverse('blog_page')
        resolver = resolve(url)
        self.assertEquals(resolver.func.view_class, BlogPage)
        self.assertEquals(resolver.func.view_class.queryset.model, Post)
        self.assertEquals(
            resolver.func.view_class.template_name, 'blog/blog.html'
            )
        self.assertEquals(
            resolver.func.view_class.context_object_name, 'all_posts'
            )
        self.assertEquals(resolver.func.view_class.paginate_by, 5)
