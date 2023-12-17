from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from chat.models import Conversation, User


class RemoveConversationTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])

    def act(self, pk_conversation):
        url = reverse("conversations-detail", args=[pk_conversation])
        self.response = self.client.delete(url)

    def test_it_returns_204_status_code_if_conversation_exists(self):
        self.act(self.conversation_1.pk)
        self.assertEqual(self.response.status_code, 204)

    def test_it_returns_404_status_code_if_conversation_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)

    def test_conversation_was_deleted(self):
        self.act(self.conversation_1.pk)
        conversation = Conversation.objects.filter(pk=self.conversation_1.pk)
        self.assertEqual(conversation.count(), 0)