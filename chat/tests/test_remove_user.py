from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from chat.models import User


class RemoveUsersTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")

    def act(self, pk=None):
        pk = pk or self.user.pk
        url = reverse("users-detail", args=[pk])
        self.response = self.client.delete(url)

    def test_it_returns_404_if_user_doesnt_exist(self):
        self.act(123456)
        self.assertEqual(self.response.status_code, 404)

    def test_it_returns_204_if_user_exists_and_was_removed(self):
        self.act()
        self.assertEqual(self.response.status_code, 204)

    def test_user_was_removed(self):
        self.act()
        user_query = User.objects.filter(pk=self.user.pk)
        self.assertEqual(len(user_query), 0)
    