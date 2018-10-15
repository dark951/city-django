from rest_framework.routers import SimpleRouter

from rbac.api.viewsets import ActionViewSet, ActionToRoleViewSet, GroupToRoleViewSet, RoleViewSet

router = SimpleRouter()
router.register(r'roles', RoleViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'role/(?P<role_id>[\d]+)/actions', ActionToRoleViewSet, 'actions_to_role')
router.register(r'role/(?P<role_id>[\d]+)/groups', GroupToRoleViewSet, 'groups_to_role')
