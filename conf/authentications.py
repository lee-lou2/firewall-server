from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from apps.device.models import Device


class MacAddressAuthentication(BaseAuthentication):
    """맥 주소 인증"""

    def authenticate(self, request):
        hashed_mac_address = request.META.get("HTTP_X_HASHED_MAC_ADDRESS")
        if not hashed_mac_address:
            return None
        device = Device.objects.filter(
            hashed_mac_address=hashed_mac_address, is_active=True
        ).first()
        if not device:
            raise exceptions.AuthenticationFailed("Invalid mac address")
        return None, device
