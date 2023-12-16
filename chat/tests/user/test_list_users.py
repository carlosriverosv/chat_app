from django.test import TestCase
from unittest.mock import patch
from chat.models import User 
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializer import UserSerializer


class TestListUsers(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")

    def act(self, url=None):
        url = reverse("users-list") if not url else url
        self.response = self.client.get(url)
        self.json_response = self.response.json()

    @patch("chat.models.User.objects")
    def test_it_returns_empty_list_if_no_users(self, mocked_user_class):
        mocked_user_class.all.return_value = User.objects.none()
        self.act()
        self.assertEqual(self.json_response, [])

    def test_it_returns_one_user(self):
        self.client.force_authenticate(user=self.user)
        self.act()
        self.assertEqual(len(self.json_response), 1)
        self.assertEqual(self.json_response, [UserSerializer(self.user).data])

    def test_it_returns_status_code_200(self):
        self.act()
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_multiple_users(self):
        self.user_2 = User.objects.create(first_name="test_2", last_name="user_2", email="test_2@user_2.com", username="test_user_2")
        self.act()
        self.assertEqual(self.json_response, [UserSerializer(self.user).data, UserSerializer(self.user_2).data])
    
    def test_it_returns_right_fields(self):
        self.act()
        user_returned = self.json_response[0]
        self.assertIn("pk", user_returned)
        self.assertIn("first_name", user_returned)
        self.assertIn("last_name", user_returned)
        self.assertIn("email", user_returned)
        self.assertIn("is_active", user_returned)
