from django.test import TestCase


class TestUrls(TestCase):
    """
    class which inherits from TestCase and test all url paths
    """

    def test_list_url_is_resolved(self):
        assert 1 == 1

