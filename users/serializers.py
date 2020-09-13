from rest_framework import serializers
from users.models import CustomUser


class UserCreateSerializer(serializers.ModelSerializer):
    """ Serializer for user registration endpoint. """

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "about", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """ Serializer for user data updates endpoint. """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "about", "email")


class UserListSerializer(serializers.ModelSerializer):
    """ Serializer for list of users endpoint. """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name", "last_name", "about", "email")


class ChangePasswordSerializer(serializers.Serializer):
    """ Serializer for password change endpoint. """

    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
