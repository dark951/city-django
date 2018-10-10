# Generated by Django 2.1.2 on 2018-10-09 07:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rbac', '0002_auto_20181008_1640'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserToRole',
            new_name='RoleToUser',
        ),
        migrations.AlterModelOptions(
            name='roletouser',
            options={'verbose_name': 'Rola do użytkownika', 'verbose_name_plural': 'Role do Użytkowników'},
        ),
    ]