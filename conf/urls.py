from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("apps.domain.v1.urls")),
    path("v1/", include("apps.audit.v1.urls")),
]
