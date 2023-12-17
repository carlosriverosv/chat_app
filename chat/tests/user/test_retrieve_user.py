from django.test import TestCase
from unittest.mock import patch
from chat.models import User 
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializers.user import UserSerializer


class TestRetrieveUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")

    def act(self, pk, url=None):
        url = reverse("users-detail", args=[pk]) if not url else url
        self.response = self.client.get(url)
        self.json_response = self.response.json()

    def test_it_returns_404_if_user_id_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)
        
    def test_it_returns_status_code_200_if_user_id_exists(self):
        self.act(self.user.pk)
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_a_dictionary(self):
        self.act(self.user.pk)
        self.assertIsInstance(self.json_response, dict)

    def test_it_returns_right_fields(self):
        self.act(self.user.pk)
        self.assertIn("pk", self.json_response)
        self.assertIn("first_name", self.json_response)
        self.assertIn("last_name", self.json_response)
        self.assertIn("email", self.json_response)
        self.assertIn("is_active", self.json_response)
