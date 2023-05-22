from django.test import TestCase
from other_pages.models import Value


class ValueModelTest(TestCase):
    """
    Class to test Value model
    """
    def test_value_model_fields(self):
        # Create a Value object
        value = Value.objects.create(
            featured_image='image.jpg',
            image_description='some image description',
            title='this is a tittle',
            content='some dummy text'
        )

        # Assert the field values
        self.assertEqual(value.featured_image, 'image.jpg')
        self.assertEqual(value.image_description, 'some image description')
        self.assertEqual(value.title, 'this is a tittle')
        self.assertEqual(value.content, 'some dummy text')
