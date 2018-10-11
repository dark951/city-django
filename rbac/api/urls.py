from rest_framework.routers import SimpleRouter

from rbac.api.viewsets import ActionViewSet, RoleViewSet

router = SimpleRouter()
router.register(r'roles', RoleViewSet)
router.register(r'actions', ActionViewSet)
