from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.audit.models import AuditLog


class CurrentDeviceDefault(CurrentUserDefault):
    """디바이스 기본값"""

    def __call__(self, serializer_field):
        return serializer_field.context["request"].auth


class AuditLogSerializer(serializers.ModelSerializer):
    """감사 로그 시리얼라이저"""

    device = serializers.HiddenField(default=CurrentDeviceDefault())

    class Meta:
        model = AuditLog
        fields = [
            "id",
            "device",
            "request_time",
            "request_url",
            "is_success",
        ]
