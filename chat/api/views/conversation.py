from rest_framework import viewsets
from chat.api.serializer import ConversationSerializer
from chat.models import Conversation



class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

        