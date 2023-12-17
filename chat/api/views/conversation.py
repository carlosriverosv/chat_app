from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from chat.api.serializers.conversation import ConversationSerializer
from chat.models import Conversation, User


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=True, methods=['put'])
    def add_user(self, request, pk=None, user_id=None):
        conversation = self.get_object()
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        conversation.users.add(user)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data)
        