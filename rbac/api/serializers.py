from rest_framework import serializers

from rbac.models import Role, Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'modified_at')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'modified_at')
