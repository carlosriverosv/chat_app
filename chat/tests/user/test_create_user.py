from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class CreateUserTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {"first_name": "test", "last_name": "user", "password": "1234567", "username": "user_test", "email": "test@user.com"}

    def act(self, url=None, data=None):
        url = reverse("users-list") or url
        data = data or {}
        self.response = self.client.post(url, data=data)
        self.json_response = self.response.json()

    def test_it_returns_status_code_201_if_payload_is_valid(self):
        self.act(data=self.data)
        self.assertEqual(self.response.status_code, 201)

    def test_it_returns_status_code_400_if_payload_is_invalid(self):
        self.data["email"] = "invalida_email.com"
        self.act(data=self.data)
        self.assertEqual(self.response.status_code, 400)

    def test_it_returns_recently_created_user(self):
        self.act(data=self.data)
        self.assertIsInstance(self.json_response, dict)
        self.assertEqual(self.json_response["first_name"], self.data["first_name"])
        self.assertEqual(self.json_response["last_name"], self.data["last_name"])
        self.assertEqual(self.json_response["email"], self.data["email"])
        self.assertEqual(self.json_response["username"], self.data["username"])
