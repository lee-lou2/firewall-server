from datetime import timedelta

from django.db import models
from django.utils import timezone


class Device(models.Model):
    """디바이스"""

    alias = models.CharField(max_length=100, verbose_name="별칭")
    hashed_mac_address = models.CharField(
        max_length=255, unique=True, verbose_name="해싱된 MAC주소"
    )
    is_active = models.BooleanField(default=True, verbose_name="활동 여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    @classmethod
    def get_devices_without_recent_access(cls, minutes=10):
        inactive_devices = cls.objects.filter(is_active=True).exclude(
            deviceaccesslog__updated_at__gte=timezone.now() - timedelta(minutes=minutes)
        )
        return inactive_devices

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"


class DeviceAccessLog(models.Model):
    """디바이스 접속 로그"""

    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, verbose_name="디바이스"
    )
    consecutive_count = models.PositiveIntegerField(default=1, verbose_name="연속 개수")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    @classmethod
    def increment_consecutive_count(cls, device: Device):
        # 현재 시간이 updated_at 보다 1분 미만일 때 연속이라 판단
        last_access_log = (
            cls.objects.filter(device=device)
            .filter(updated_at__gte=timezone.now() - timedelta(minutes=1))
            .order_by("-updated_at")
            .first()
        )
        if not last_access_log:
            return cls.objects.create(device=device)
        last_access_log.consecutive_count += 1
        last_access_log.save()
        return last_access_log

    class Meta:
        verbose_name = "Device Access Log"
        verbose_name_plural = "Device Access Logs"
        indexes = [
            models.Index(
                fields=["device", "-updated_at"], name="device_updated_at_desc_idx"
            ),
        ]
