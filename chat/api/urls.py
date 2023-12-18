from rest_framework.routers import DefaultRouter
from django.urls import path, include
from chat.api.views.conversation import ConversationViewSet
from chat.api.views.message import MessageViewSet
from chat.api.views.user import UsersViewSet


router = DefaultRouter(
    trailing_slash=False,
)
router.register(r"users", UsersViewSet, basename="users",)
router.register(r"conversations", ConversationViewSet, basename="conversations")
router.register(r"messages", MessageViewSet, basename="messages")

urlpatterns = [
    path("", include(router.urls)),
    path("conversations/<int:pk>/user/<int:user_id>", ConversationViewSet.as_view({'put': 'add_user'}), name='conversation-add-user'),
]