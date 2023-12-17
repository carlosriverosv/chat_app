from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializer import ConversationSerializer

from chat.models import Conversation, User


class ListConversationsTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.user_2 = User.objects.create(first_name="test_2", last_name="user_2", email="test_2@user_2.com", username="test_user_2")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])
        self.conversation_2 = Conversation.objects.create()
        self.conversation_2.users.set([self.user, self.user_2])


    def act(self):
        url = reverse("conversations-list")
        self.response = self.client.get(url)
        self.json_response = self.response.json()

    def test_it_returns_status_code_200(self):
        self.act()
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_a_list(self):
        self.act()
        self.assertIsInstance(self.json_response, list)

    def test_it_returns_all_conversations(self):
        self.act()
        self.assertEqual(len(self.json_response), 2)
        self.assertEqual(self.json_response, [ConversationSerializer(self.conversation_1).data, ConversationSerializer(self.conversation_2).data])
