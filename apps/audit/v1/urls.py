from rest_framework.routers import SimpleRouter

from apps.audit.v1.views import AuditLogViewSet

router = SimpleRouter()
router.register(r"audit-logs", AuditLogViewSet, basename="audit-logs")

urlpatterns = router.urls
