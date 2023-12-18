from rest_framework import viewsets
from chat.api.serializers.message import MessageSerializer
from chat.models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
