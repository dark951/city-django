# Generated by Django 2.1.2 on 2018-10-04 13:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupToRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Grupa do roli',
                'verbose_name_plural': 'Grupy do ról',
            },
        ),
        migrations.CreateModel(
            name='PermissionToRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
            options={
                'verbose_name': 'Uprawnienie do roli',
                'verbose_name_plural': 'Uprawnienia do ról',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('name', models.CharField(max_length=512, unique=True, verbose_name='Nazwa')),
                ('active', models.BooleanField(default=True, verbose_name='Aktywna')),
            ],
            options={
                'verbose_name': 'Rola',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='UserToRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Użytkownik do roli',
                'verbose_name_plural': 'Użytkownicy do ról',
            },
        ),
        migrations.AddField(
            model_name='permissiontorole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role'),
        ),
        migrations.AddField(
            model_name='grouptorole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role'),
        ),
        migrations.AlterUniqueTogether(
            name='permissiontorole',
            unique_together={('role', 'permission')},
        ),
    ]
