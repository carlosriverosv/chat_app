from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializers.message import MessageSerializer

from chat.models import Conversation, Message, User


class RetrieveMessageConversationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])
        self.message = Message.objects.create(message_text="hello!", user=self.user, conversation=self.conversation_1)

        self.conversation_2 = Conversation.objects.create()
        self.conversation_2.users.set([self.user])
        self.message_2 = Message.objects.create(message_text="Hi", user=self.user, conversation=self.conversation_2)

    def act(self, conversation_pk):
        url = reverse("conversations-messages", args=[conversation_pk])
        self.response = self.client.get(url)
        self.response_json = self.response.json()

    def test_it_returns_status_code_200(self):
        self.act(self.conversation_1.pk)
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_a_list(self):
        self.act(self.conversation_1.pk)
        self.assertIsInstance(self.response_json, list)

    def test_it_returns_status_code_404_if_conversation_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)

    def test_it_returns_messages_from_the_expected_conversation(self):
        self.act(self.conversation_1.pk)
        self.assertEqual(len(self.response_json), 1)
        self.assertEqual(self.response_json, [MessageSerializer(self.message).data])
