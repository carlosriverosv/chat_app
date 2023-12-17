from django.contrib.auth import get_user_model
from chat.models import User
from rest_framework import serializers


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
            'username',
        ]
        read_only_fields = [
            "pk"
        ]
