from chat.models import User
from chat.api.serializer import UserSerializer
from django.db.models.query import QuerySet
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404


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
    
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            object_serialized = UserSerializer(user)
            return Response(object_serialized.data)
        except User.DoesNotExist:
            raise Http404
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def results_paginated(self, users: QuerySet):
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
