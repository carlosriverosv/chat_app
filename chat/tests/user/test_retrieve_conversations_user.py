from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from chat.models import Conversation, User


class RetrieveConversationsUserTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])

    def act(self, user_pk):
        url = reverse("users-conversations", args=[user_pk])
        self.response = self.client.get(url)
        self.response_json = self.response.json()

    def test_it_returns_status_code_200(self):
        self.act(self.user.pk)
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_a_list(self):
        self.act(self.user.pk)
        self.assertIsInstance(self.response_json, list)

    def test_it_returns_an_empty_list_if_user_doesnt_have_conversations(self):
        self.user_2 = User.objects.create(first_name="test_2", last_name="user_2", email="test2@user.com", username="test_user_2")
        self.act(self.user_2.pk)
        self.assertIsInstance(self.response_json, list)
        self.assertEqual(len(self.response_json), 0)

    def test_it_returns_status_code_404_if_user_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)
