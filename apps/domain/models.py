from django.db import models


class Domain(models.Model):
    """허용 도메인"""

    domain = models.CharField(max_length=255, unique=True, verbose_name="도메인")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"


class DeviceAllowedDomain(models.Model):
    """디바이스에 대한 허용 도메인"""

    device = models.ForeignKey(
        "device.Device", on_delete=models.CASCADE, verbose_name="디바이스"
    )
    allowed_domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, verbose_name="허용 도메인"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")

    def __str__(self):
        return f"{self.device} - {self.allowed_domain}"

    class Meta:
        verbose_name = "Device Allowed Domain"
        verbose_name_plural = "Device Allowed Domains"
        unique_together = ["device", "allowed_domain"]
