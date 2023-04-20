from django.test import TestCase

# Create your tests here.
class TestMyApp(TestCase):
    def setUp(self):
        print("My Setup Method")
        pass

    def test_if_this_is_true(self):
        print("Yes it is true")
        self.assertTrue(True)

    def test_if_this_is_false(self):
        print("Yes it is false")
        self.assertFalse(False)