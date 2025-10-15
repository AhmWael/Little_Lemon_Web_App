from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Pizza", price=120, inventory=50)
        MenuItem.objects.create(title="Pasta", price=80, inventory=30)

    def test_get_all_menu_items(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Pizza")
        self.assertEqual(response.data[1]['title'], "Pasta")
