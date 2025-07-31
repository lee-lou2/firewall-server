from rest_framework import views, response

from apps.device.models import DeviceAccessLog
from apps.domain.models import Domain
from conf.authentications import MacAddressAuthentication
from conf.permissions import IsActiveDevice


class AllowedDomainAPIView(views.APIView):
    """디바이스 허용 도메인 뷰"""

    authentication_classes = [MacAddressAuthentication]
    permission_classes = [IsActiveDevice]

    def get(self, request, *args, **kwargs):
        domains = Domain.objects.filter(
            devicealloweddomain__device=request.auth
        ).values_list("domain", flat=True)
        # 접속 기록
        DeviceAccessLog.increment_consecutive_count(request.auth)
        return response.Response({"results": list(set(domains))})
