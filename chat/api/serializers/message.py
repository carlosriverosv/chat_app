from rest_framework import serializers
from chat.models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):

    def validate(self, data):
        user = data["user"]
        conversation = data["conversation"]
        user_in_conversation = conversation.users.filter(pk__in=[user.pk])
        if not user_in_conversation:
            raise serializers.ValidationError("User is not in this conversation")
        return data

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['date_created']
