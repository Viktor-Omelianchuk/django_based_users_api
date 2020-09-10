from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from users.models import CustomUser
from users.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer
from users.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UsersListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    # renderer_classes = [JSONRenderer]



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)

