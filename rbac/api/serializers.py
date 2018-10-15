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


class ActionToRoleSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        actions = {
            'list': '_list_action_fields',
            'create': '_create_action_fields'
        }
        try:
            getattr(self,actions[kwargs.get('context').get('view').action])()
        except KeyError:
            pass

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def _list_action_fields(self):
        self.fields['id'] = serializers.IntegerField()
        self.fields['action_id'] = serializers.IntegerField()

    def _create_action_fields(self):
        self.fields['action_id'] = serializers.IntegerField(required=True)


class GroupToRoleSerializer(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('context').get('view').action is 'list':
            self.fields['id'] = serializers.IntegerField()
            self.fields['group_id'] = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
