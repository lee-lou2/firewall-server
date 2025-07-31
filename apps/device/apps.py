from django.apps import AppConfig


class DeviceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.device"

    def ready(self):
        from apps.device.v1 import schedulers

        schedulers.start()
