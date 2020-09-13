from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from users.views import *


app_name = 'user'
urlpatterns = [
    path('user/registration/', UserCreateView.as_view()),
    path('user/all_users/', UsersListView.as_view(), name='all_users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token-auth/', views.obtain_auth_token),
]

