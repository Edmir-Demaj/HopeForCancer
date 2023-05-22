from django.test import TestCase
from contact.models import Contact, FAQ


class ContactModelTest(TestCase):
    """
    Class to test Contact model
    """
    def setUp(self):
        # create a contact form with fields
        self.contact = Contact.objects.create(
            name='user 3',
            email='mail@example.com',
            subject='some subject',
            content='some content',
        )

    def test_contact_model_fields(self):
        # validate each field input
        self.assertEqual(self.contact.name, 'user 3')
        self.assertEqual(self.contact.email, 'mail@example.com')
        self.assertEqual(self.contact.subject, 'some subject')
        self.assertEqual(self.contact.content, 'some content')
        self.assertIsNotNone(self.contact.created_date)


class FAQModelTest(TestCase):
    """
    Class to test FAQ model
    """

    def setUp(self):
        # create an instance of faq model
        self.faq = FAQ.objects.create(
            title='Test FAQ',
            content='Test FAQ content',
        )

    def test_faq_model_fields(self):
        # validate faq fields
        self.assertEqual(self.faq.title, 'Test FAQ')
        self.assertEqual(self.faq.content, 'Test FAQ content')
