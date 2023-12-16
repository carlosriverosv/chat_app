from rest_framework.routers import DefaultRouter
from chat.api.views.conversation import ConversationViewSet
from chat.api.views.user import UsersViewSet


router = DefaultRouter(
    trailing_slash=False,
)
router.register(r"users", UsersViewSet, basename="users",)
router.register(r"conversations", ConversationViewSet, basename="conversations")

urlpatterns = router.urls
