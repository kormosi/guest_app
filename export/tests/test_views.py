from django.test import TestCase
from django.urls import reverse
from export import views


class ViewsTest(TestCase):

    def test_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('export-home'))
        self.assertEqual(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'export/index.html')


    def test_post_request_returns_200(self):
        response = self.client.post('')
        self.assertEqual(response.status_code, 200)


    def test_post_request_returns_PDF(self):
        response = self.client.post('')
        self.assertEqual(response['content-type'], 'application/pdf')
