from django.test import TestCase
from django.urls import reverse, resolve
from other_pages.views import *


class OtherpagesAppTestUrls(TestCase):
    """
    Subclass which inherits from TestCase class and tests all urls
    """

    def test_home_page_url(self):
        # Check if the URL resovels to the 'index' view function
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_about_page_url(self):
        # Check if the URL resovels to the 'about_page' view function
        url = reverse('about')
        self.assertEquals(resolve(url).func, about_page)

    def test_info_page_url(self):
        # Check if the URL resovels to the 'info_page' view function
        url = reverse('info')
        self.assertEquals(resolve(url).func, info_page)
