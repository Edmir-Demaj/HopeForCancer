from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import *


class TestCategoryModel(TestCase):
    """
    Inside this class will test category model used in blog app
    and the meta class
    """
    def test_creating_new_category_model_(self):
        # test when a new category is created
        new_category = Category.objects.create(
            category_name='testing category',
            slug='testing-category',
        )
        self.assertEqual(new_category.category_name, 'testing category')
        self.assertEqual(new_category.slug, 'testing-category')

    def test_verbose_names(self):
        # test if category model verbose names are added properly
        self.assertEqual(str(
            Category._meta.verbose_name), "Category")
        self.assertEqual(str(
            Category._meta.verbose_name_plural), "Categories")


class TestPostModel(TestCase):
    """
    Inside this class will test Post model used in blog app
    and the meta class
    """
    def setUp(self):
        # first create a user and category instances and after
        # create a new test post
        user = User.objects.create_user(username='testuser', password='test13')
        category = Category.objects.create(
            category_name='Personal Stories', slug='personal-stories'
        )
        Post.objects.create(
            title='Test Post',
            slug='test-post',
            featured_image='https://res.cloudinary.com/dxlqthpli/image/upload/v1684175225/404_img_y8kemd.jpg',  # noqa: 501
            describe_image='some text',
            category=category,
            content='This is a test post',
            author=user,
            status=0,
            comment_counter=0
        )

    def test_post_model_inputs(self):
        # In this test we validate each field of the
        # post created abowe
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.featured_image.url, 'https://res.cloudinary.com/dxlqthpli/image/upload/v1684175225/404_img_y8kemd')  # noqa: 501
        self.assertEqual(post.describe_image, 'some text')
        self.assertEqual(post.category.category_name, 'Personal Stories')
        self.assertEqual(post.content, 'This is a test post')
        self.assertEqual(post.author.username, 'testuser')
        self.assertEqual(post.status, 0)
        self.assertEqual(post.comment_counter, 0)
