from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/base-auth/", include("rest_framework.urls")),
    path("api/", include("users.urls")),
    path("api/auth/", include("djoser.urls")),
    path("api/auth_token/", include("djoser.urls.authtoken")),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
