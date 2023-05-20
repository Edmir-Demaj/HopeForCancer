from django.test import TestCase
from .forms import *


class CreatePostFormTest(TestCase):

    def test_create_post_form_valid_data(self):
        form = CreatePostForm(data={
            'title': 'Test Title',
            'featured_image': 'test.jpg',
            'describe_image': 'Test image description',
            'category': 'Personal Stories',
            'content': 'Test content',
        })

        self.assertTrue(form.is_valid(), form.errors.as_text())
