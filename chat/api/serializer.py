from django.contrib.auth import get_user_model
from chat.models import Conversation, User
from rest_framework import serializers
from rest_framework.serializers import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'username'
        ]
        read_only_fields = [
            "pk"
        ]


class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['date_created']
