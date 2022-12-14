from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.apps.accounts.api.views import CustomTokenObtainPairView

urlpatterns = [
    # Admin Panel
    path("admin/", admin.site.urls),
    # Account
    path("api/user/", include("core.apps.accounts.api.urls")),
    path(
        "api/token/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    # Threads
    path("api/threads/", include("core.apps.threads.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
