from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework import viewsets

from rbac.api.serializers import ActionSerializer, RoleSerializer, ActionToRoleSerializer, GroupToRoleSerializer
from rbac.models import Action, Role, ActionToRole, GroupToRole


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('created_at', 'modified_at')
    search_fields = ('codename', 'name')
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('active',)
    search_fields = ('name',)
    ordering_fields = ('name', 'created_at', 'modified_at')
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ActionToRoleViewSet(viewsets.ModelViewSet):
    serializer_class = ActionToRoleSerializer

    def get_queryset(self):
        return ActionToRole.objects.filter(role=self.kwargs.get('role_id'))


class GroupToRoleViewSet(viewsets.ModelViewSet):
    serializer_class = GroupToRoleSerializer

    def get_queryset(self):
        return GroupToRole.objects.filter(role=self.kwargs.get('role_id'))
