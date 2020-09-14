from rest_framework import generics
from users.models import CustomUser
from users.serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserDetailSerializer,
)
from users.permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer


class UserCreateView(generics.CreateAPIView):
    """ Creates a user """

    serializer_class = UserCreateSerializer


class UsersListView(generics.ListAPIView):
    """List of users"""

    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, )


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Detailed information about the user with the ability to change data """

    serializer_class = UserDetailSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)


class ChangePasswordView(generics.UpdateAPIView):
    """ An endpoint for changing password. """

    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
