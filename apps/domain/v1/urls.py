from django.urls import path

from apps.domain.v1.views import AllowedDomainAPIView

urlpatterns = [
    path(
        "allowed-domains/",
        AllowedDomainAPIView.as_view(),
        name="allowed-domains",
    ),
]
