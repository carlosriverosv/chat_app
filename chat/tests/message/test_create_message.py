from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializers.message import MessageSerializer

from chat.models import Conversation, Message, User


class CreateMessageTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])
        self.data = {"message_text": "hello!", "conversation": self.conversation_1.pk, "user": self.user.pk}

    def act(self, data=None):
        url = reverse("messages-list")
        data = data or {}
        self.response = self.client.post(url, data)
        self.response_json = self.response.json()

    def test_it_returns_status_code_201_if_message_is_created(self):
        self.act(self.data)
        self.assertEqual(self.response.status_code, 201)

    def test_it_returns_status_code_400_if_user_doesnt_exist(self):
        self.data["user"] = 123456
        self.act(self.data)
        self.assertEqual(self.response.status_code, 400)

    def test_it_only_creates_message_if_user_is_in_conversation(self):
        user_2 = User.objects.create(first_name="test_2", last_name="user_2", email="test2@user.com", username="test_user_2")
        self.data["user"] = user_2.pk
        self.act(self.data)
        self.assertEqual(self.response.status_code, 400)

    def test_it_creates_message(self):
        self.act(self.data)
        messages = Message.objects.all()
        self.assertEqual(messages.count(), 1)
        self.assertEqual(self.response_json, MessageSerializer(messages[0]).data)
