from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("banks.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/", include("banks.api.urls", namespace="api")),
]
