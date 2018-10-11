from rest_framework import viewsets

from rbac.api.serializers import ActionSerializer, RoleSerializer
from rbac.models import Action, Role


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    search_fields = ('codename', 'name')


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_fields = ('active',)
    search_fields = ('name',)
