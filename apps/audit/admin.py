from django.contrib import admin, messages
from django.utils.dateparse import parse_datetime

from apps.domain.models import DeviceAllowedDomain, Domain
from apps.audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        "device",
        "request_time",
        "request_url",
        "is_success",
    )
    list_filter = (
        "device",
        "request_time",
        "is_success",
    )
    search_fields = ("device__alias", "request_url")
    search_help_text = "장치 별칭, 요청 URL 또는 날짜/시간 범위로 검색할 수 있습니다. (예: '2025-07-30 10:00 to 2025-07-30 11:00')"
    actions = ("add_to_allowed_domains",)

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            try:
                if " to " in search_term:
                    start_str, end_str = search_term.split(" to ", 1)
                    start_dt = parse_datetime(start_str.strip())
                    end_dt = parse_datetime(end_str.strip())
                    if start_dt and end_dt:
                        return (
                            queryset.filter(request_time__range=(start_dt, end_dt)),
                            False,
                        )
            except (ValueError, TypeError):
                pass
        return super().get_search_results(request, queryset, search_term)

    @admin.action(description="선택된 로그의 요청 URL을 허용 도메인에 추가")
    def add_to_allowed_domains(self, request, queryset):
        added_count = 0
        for log in queryset:
            if not log.request_url:
                continue
            domain, _ = Domain.objects.get_or_create(domain=log.request_url)
            _, created = DeviceAllowedDomain.objects.get_or_create(
                device=log.device, allowed_domain=domain
            )
            if created:
                added_count += 1

        self.message_user(
            request,
            f"총 {added_count}개의 도메인이 허용 목록에 새로 추가되었습니다.",
            level=messages.SUCCESS,
        )
