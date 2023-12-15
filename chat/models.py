from django.contrib.auth.models import AbstractUser
from django.db import models


class Conversation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField("User")


class User(AbstractUser):
    pass


class Message(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    multimedia_url = models.CharField(max_length=2048)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
