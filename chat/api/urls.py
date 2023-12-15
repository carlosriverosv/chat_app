from rest_framework.routers import DefaultRouter
from chat.api.views import UsersViewSet


router = DefaultRouter(
    trailing_slash=False,
)
router.register(
    r'users', UsersViewSet, basename='users',
)

urlpatterns = router.urls
