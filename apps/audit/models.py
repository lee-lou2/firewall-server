from django.db import models


class AuditLog(models.Model):
    """감사 로그"""

    device = models.ForeignKey(
        "device.Device", on_delete=models.DO_NOTHING, verbose_name="디바이스"
    )
    request_time = models.DateTimeField(db_index=True, verbose_name="요청 시간")
    request_url = models.CharField(max_length=255, verbose_name="요청 주소")
    is_success = models.BooleanField(default=False, verbose_name="성공 여부")

    def __str__(self):
        return f"{self.device} - {self.request_time}"

    class Meta:
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"
