from django.contrib import admin
from django.urls import path, include

from users.views import *


app_name = 'user'
urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/all_users/', UsersListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]

