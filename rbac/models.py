from django.contrib.auth import get_user_model
from django.contrib.auth.models import (Group, Permission)
from django.db import models

from common.models import Timestamped


class Role(Timestamped):
    """
    Model represents user role in the application.
    The user can be attached to many different roles.
    """
    name = models.CharField('Nazwa', max_length=512, unique=True)
    active = models.BooleanField('Aktywna', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class PermissionToRole(Timestamped):
    """
    Model contains connection data between a role and a permission
    It has a unique index on the role-group dyad.
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Uprawnienie do roli'
        verbose_name_plural = 'Uprawnienia do ról'
        unique_together = ['role', 'permission']


class GroupToRole(Timestamped):
    """
    Model contains connection data between a role and an group of the permissions.
    It has a unique index on the role-group dyad.
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Grupa do roli'
        verbose_name_plural = 'Grupy do ról'
        unique_together = ['role', 'group']


class UserToRole(Timestamped):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Użytkownik do roli'
        verbose_name_plural = 'Użytkownicy do ról'
        unique_together = ['role', 'user']
