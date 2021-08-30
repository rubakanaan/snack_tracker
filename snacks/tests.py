from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class SnackTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status_code(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_templete(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')