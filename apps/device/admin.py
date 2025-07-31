import hashlib

from django import forms
from django.conf import settings
from django.contrib import admin

from apps.device.models import Device


class DeviceAdminForm(forms.ModelForm):
    mac_address = forms.CharField(
        label="MAC 주소",
        required=False,
        help_text="MAC 주소를 변경하려면 여기에 새 주소를 입력하세요. 비워두면 기존 주소가 유지됩니다.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance or not self.instance.pk:
            self.fields["mac_address"].required = True
            self.fields["mac_address"].help_text = "디바이스의 MAC 주소를 입력하세요."

    def save(self, commit=True):
        mac_address = self.cleaned_data.get("mac_address")
        if mac_address:
            salt = settings.HASH_SALT
            hashed_mac_address = hashlib.sha256(
                (mac_address + salt).encode()
            ).hexdigest()
            self.instance.hashed_mac_address = hashed_mac_address
        return super().save(commit)

    class Meta:
        model = Device
        fields = ["alias"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm
    list_display = ("alias", "hashed_mac_address", "created_at", "updated_at")
    readonly_fields = ("hashed_mac_address",)
    fields = ("alias", "mac_address", "hashed_mac_address")
