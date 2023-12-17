from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from chat.models import Conversation, User


class TestAddUserToConversation(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.user_2 = User.objects.create(first_name="test_2", last_name="user_2", email="test_2@user2.com", username="test_user_2")
        self.conversation_1 = Conversation.objects.create()
        self.conversation_1.users.set([self.user])

    def act(self, pk_conversation, pk_user_to_add):
        url = reverse("conversation-add-user", args=[pk_conversation, pk_user_to_add])
        self.response = self.client.put(url)

    def test_add_user_to_existent_conversation_returns_200(self):
        self.act(self.conversation_1.pk, self.user_2.pk)
        self.assertEqual(self.response.status_code, 200)

    def test_it_adds_user_to_conversation(self):
        self.act(self.conversation_1.pk, self.user_2.pk)
        users_in_conversation = Conversation.objects.filter(pk=self.conversation_1.pk)[0].users.count()
        self.assertEqual(users_in_conversation, 2)

    def test_it_returns_status_code_404_if_user_doesnt_exist(self):
        self.act(self.conversation_1.pk, 123456)
        self.assertEqual(self.response.status_code, 404)
        self.assertEqual(self.response.json()["error"], "User not found")

    def test_it_returns_status_code_404_if_conversation_doesnt_exist(self):
        self.act(1234565, self.user_2.pk)
        self.assertEqual(self.response.status_code, 404)
