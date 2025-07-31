from django import forms
from django.contrib import admin
from apps.domain.models import Domain, DeviceAllowedDomain


class DeviceAllowedDomainForm(forms.ModelForm):
    domain = forms.CharField(
        label="도메인", help_text="입력한 도메인이 없으면 새로 생성됩니다."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["domain"].initial = self.instance.allowed_domain.domain

    def save(self, commit=True):
        domain_name = self.cleaned_data.get("domain")
        if domain_name:
            domain, _ = Domain.objects.get_or_create(domain=domain_name)
            self.instance.allowed_domain = domain
        return super().save(commit)

    class Meta:
        model = DeviceAllowedDomain
        fields = ["device"]


@admin.register(DeviceAllowedDomain)
class DeviceAllowedDomainAdmin(admin.ModelAdmin):
    form = DeviceAllowedDomainForm
    list_display = ["device", "allowed_domain", "created_at"]
