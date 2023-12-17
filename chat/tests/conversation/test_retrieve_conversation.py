from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from chat.api.serializers.conversation import ConversationSerializer

from chat.models import Conversation, User


class RetrieveConversationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])

    def act(self, conversation_pk):
        url = reverse("conversations-detail", args=[conversation_pk])
        self.response = self.client.get(url)
        self.response_json = self.response.json()

    def test_it_returns_200_status_code_if_conversation_exists(self):
        self.act(self.conversation_1.pk)
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_a_dict(self):
        self.act(self.conversation_1.pk)
        self.assertIsInstance(self.response_json, dict)

    def test_it_returns_right_conversation(self):
        self.act(self.conversation_1.pk)
        self.assertEqual(self.response_json, ConversationSerializer(self.conversation_1).data)

    def test_it_returns_expected_fields(self):
        self.act(self.conversation_1.pk)
        self.assertIn("date_created", self.response_json)
        self.assertIn("users", self.response_json)
        self.assertIn("id", self.response_json)

    def test_it_returns_404_status_code_if_conversation_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)
