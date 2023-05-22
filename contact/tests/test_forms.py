from django.test import TestCase
from contact.forms import *


class ContactAppTestForms(TestCase):
    """
    This class test all forms used in contact app first when they have data
    inserted and secondly when they don't have data inserted
    """
    def test_contact_form_valid_data(self):
        # test the form with data inserted
        form = ContactForm(data={
            'name': 'user1',
            'email': 'mymail@gmail.com',
            'subject': 'some text',
            'content': 'This is a personal message',
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_novalid_data(self):
        # test the form when has no data inserted
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
