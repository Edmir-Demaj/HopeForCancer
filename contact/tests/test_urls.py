from django.test import TestCase
from django.urls import reverse, resolve
from contact.views import contact


class ContactAppTestUrls(TestCase):
    """
    Subclass which inherits from TestCase class and tests all urls
    """

    def test_contact_page_url(self):
        # Check if the URL resovels to the 'contact' view function
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
