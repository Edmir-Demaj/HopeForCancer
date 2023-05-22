from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import *


class BlogAppTestUrls(TestCase):
    """
    Subclass which inherits from TestCase class and tests all urls
    """

    def test_blog_page_url(self):
        # Check if the URL resovels to the 'BlogPage' view class
        url = reverse('blog_page')
        self.assertEquals(resolve(url).func.view_class, BlogPage)

    def test_post_detail_page_url(self):
        # Check if the URL resovels to the 'postDetail' view method
        url = reverse('post_detail', args=['slug'])
        self.assertEquals(resolve(url).func, postDetail)

    def test_create_post_page_url(self):
        # Check if the URL resovels to the 'CreatePost' view class
        url = reverse('create-post')
        self.assertEquals(resolve(url).func.view_class, CreatePost)

    def test_update_post_page_url(self):
        # Check if the URL resovels to the 'update_post' view function
        url = reverse('update-post', args=['slug'])
        self.assertEquals(resolve(url).func, update_post)

    def test_delete_post_url(self):
        # Check if the URL resovels to the 'DeletePost' view class
        url = reverse('delete-post', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, DeletePost)

    def test_like_post_url(self):
        # Check if the URL resovels to the 'PostLike' view class
        url = reverse('post_like', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_add_comment_url(self):
        # Check if the URL resovels to the 'add_comment' view function
        url = reverse('add_comment', args=['4'])
        self.assertEquals(resolve(url).func, add_comment)

    def test_edit_comment_page_url(self):
        # Check if the URL resovels to the 'EditComment' view class
        url = reverse('edit_comment', args=['4'])
        self.assertEquals(resolve(url).func.view_class, EditComment)

    def test_delete_comment_page_url(self):
        # Check if the URL resovels to the 'EditComment' view class
        url = reverse('delete_comment', args=['4'])
        self.assertEquals(resolve(url).func, delete_comment)
