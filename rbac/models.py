from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models

from common.models import Timestamped


class Action(Timestamped):
    """
    Model represents action for rbac.
    """
    name = models.CharField('Nazwa', max_length=64)
    codename = models.CharField('Akcja', max_length=100)

    def __str__(self):
        return "{0}({1})".format(self.name, self.codename)

    class Meta:
        verbose_name = 'Akcja'
        verbose_name_plural = 'Akcje'
        unique_together = ('name', 'codename')


class ActionToGroup(Timestamped):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}[{1}]".format(str(self.action), str(self.group))

    class Meta:
        verbose_name = 'Uprawnienie do grupy'
        verbose_name_plural = 'Uprawnienia do grup'
        unique_together = ('group', 'action')


class ActionToRole(Timestamped):
    """
    Model contains connection data between a role and a permission
    It has a unique index on the role-group dyad.
    """
    role = models.ForeignKey('rbac.Role', on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}[{1}]".format(str(self.action), str(self.role))

    class Meta:
        verbose_name = 'Uprawnienie do roli'
        verbose_name_plural = 'Uprawnienia do ról'
        unique_together = ('role', 'action')


class GroupToRole(Timestamped):
    """
    Model contains connection data between a role and an group of the permissions.
    It has a unique index on the role-group dyad.
    """
    role = models.ForeignKey('rbac.Role', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}[{1}]".format(str(self.group), str(self.role))

    class Meta:
        verbose_name = 'Grupa do roli'
        verbose_name_plural = 'Grupy do ról'
        unique_together = ['role', 'group']


class Role(Timestamped):
    """
    Model represents user role in the application.
    The user can be attached to many different roles.
    """
    name = models.CharField('Nazwa', max_length=64, unique=True)
    active = models.BooleanField('Aktywna', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class RoleToUser(Timestamped):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "{0}[{1}]".format(str(self.role), str(self.user))

    class Meta:
        verbose_name = 'Rola do użytkownika'
        verbose_name_plural = 'Role do Użytkowników'
        unique_together = ['role', 'user']
