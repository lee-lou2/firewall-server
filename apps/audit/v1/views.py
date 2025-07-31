from rest_framework import viewsets, mixins

from apps.audit.v1.serializers import AuditLogSerializer
from conf.authentications import MacAddressAuthentication
from conf.permissions import IsActiveDevice


class AuditLogViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """감사 로그 뷰셋"""

    authentication_classes = [MacAddressAuthentication]
    permission_classes = [IsActiveDevice]
    serializer_class = AuditLogSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
