from rest_framework.permissions import BasePermission


class IsActiveDevice(BasePermission):
    """활성 디바이스 권한"""

    def has_permission(self, request, view):
        return bool(request.auth and request.auth.is_active)
