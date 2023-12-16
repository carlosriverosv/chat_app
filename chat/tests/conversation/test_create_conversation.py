from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from chat.models import User

class CreateConversationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")

    def act(self, url=None, data=None):
        url = reverse("conversations-list") or url
        data = data or {}
        self.response = self.client.post(url, data=data)
        self.json_response = self.response.json()

    def test_it_returns_status_code_201_if_conversation_was_created(self):
        self.act(data={"users": [self.user.pk]})
        self.assertEqual(self.response.status_code, 201)

    def test_it_returns_conversation_created(self):
        self.act(data={"users": [self.user.pk]})
        self.assertIn("id", self.json_response)
        self.assertIn("date_created", self.json_response)
        self.assertIn("users", self.json_response)
    
    def test_it_returns_status_code_400_if_user_id_doesnt_exist(self):
        self.act(data={"users": [self.user.pk, 11111]})
        self.assertEqual(self.response.status_code, 400)