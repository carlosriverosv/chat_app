from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


from chat.models import User

class UpdateUsersTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name="test", last_name="user", email="test@user.com", username="test_user_1")
        self.data = {"email": "new_email@user.com", "username": "test_user_1"}

    def act(self, pk, data=None):
        data = data or {}
        url = reverse("users-detail", args=[pk])
        self.response = self.client.put(url, data)
        self.response_json = self.response.json()

    def test_it_returns_404_if_user_doesnt_exist(self):
        self.act(123456, self.data)
        self.assertEqual(self.response.status_code, 404)

    def test_it_returns_200_if_user_exists_and_could_be_updated(self):
        self.act(self.user.pk, self.data)
        self.assertEqual(self.response.status_code, 200)

    def test_it_returns_updated_user(self):
        self.act(self.user.pk, self.data)
        self.assertEqual(self.response_json["pk"], self.user.pk)

    def test_it_updates_the_user_info(self):
        self.act(self.user.pk, self.data)
        self.assertEqual(self.response_json["email"], "new_email@user.com")

    def test_it_validates_data_in_payload(self):
        self.data["email"] = "invalid_email.com"
        self.act(self.user.pk, self.data)
        self.assertEqual(self.response.status_code, 400)
    