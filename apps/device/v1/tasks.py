from django.conf import settings
from django.utils import timezone

from apps.common.utils import send_slack_message
from apps.device.models import Device


def recent_10_min_data_monitor():
    without_recent_access = Device.get_devices_without_recent_access(minutes=10)
    now_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    without_recent_access_str = ", ".join(
        list(without_recent_access.values_list("alias", flat=True))
    )
    message = f"[{now_str}] 10분 이내 미접속: {without_recent_access_str}"
    send_slack_message(settings.SLACK_WEBHOOK_URL, message)
