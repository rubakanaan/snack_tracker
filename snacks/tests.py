from django.test import TestCase
from django.urls import reverse , reverse_lazy
from django.contrib.auth  import get_user_model
from .models import Snack
# Create your tests here.


class SnackTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username = 'aasdghj',
            email='a@gmal.com',
            password='1234556'
            
        )  
        self.snack= Snack.objects.create(
            name = 'a',
            purchaser = self.user,
            description = 'anything '
        ) 

    def test_detail_page_status_code(self):
        url = reverse('snack_detail', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_list_page_templete(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_templete(self):
        url = reverse('snack_detail', args='1')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')