from django.test import TestCase
from blog.forms import *
from blog.models import Category


class BlogAppTestForms(TestCase):
    """
    This class test all forms used in blog app first when they have data
    inserted and secondly when they don't have data inserted
    """
    def test_create_post_form_valid_data(self):
        # test the form with data inserted
        category = Category.objects.create(category_name='Testing category')
        form = CreatePostForm(data={
            'title': 'post1',
            'featured_image': 'image.jpg',
            'describe_image': 'some text',
            'category': category.pk,
            'content': 'This is a personal post',
        })
        self.assertTrue(form.is_valid())

    def test_create_post_form_novalid_data(self):
        # test the form when has no data inserted
        form = CreatePostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_update_post_form_valid_data(self):
        # test the form with data inserted
        category = Category.objects.create(category_name='Testing updated')
        form = CreatePostForm(data={
            'title': 'post2',
            'featured_image': 'image2.jpg',
            'describe_image': 'some new text',
            'category': category.pk,
            'content': 'This is a personal post 2',
        })
        self.assertTrue(form.is_valid())

    def test_update_post_form_novalid_data(self):
        # test the form when has no data inserted
        form = CreatePostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_comment_form_valid_data(self):
        # test the form with data inserted
        form = CommentForm(data={
            'body': 'this is my comment',
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_novalid_data(self):
        # test the form when has no data inserted
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
