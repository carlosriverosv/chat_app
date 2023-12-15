from chat.models import User
from chat.api.serializer import UserSerializer
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.response import Response



class UsersViewSet(viewsets.ModelViewSet):
    """
    Endpoint for returning User data.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        return self.results_paginated(users)
        
    def results_paginated(self, users: QuerySet):
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
