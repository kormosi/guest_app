from django.test import TestCase
from export.models import Guest


class ModelsTest(TestCase):

    def setUp(self):
        self.guest = Guest.objects.create(first_name='Abraham',
                                         last_name='Lincoln',
                                         base64_image='deadbeef123456789')


    def test_guest_creation(self):
        self.assertTrue(isinstance(self.guest, Guest))


    def test_guest_repr(self):
        self.assertEqual(self.guest.__repr__(),
                        'First Name: Abraham Last Name: Lincoln')


    def test_guest_str(self):
        self.assertEqual(self.guest.__str__(), 'Abraham Lincoln')
