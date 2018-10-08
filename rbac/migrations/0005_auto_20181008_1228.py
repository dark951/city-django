# Generated by Django 2.1.2 on 2018-10-08 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('rbac', '0004_auto_20181008_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionToGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Action')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Uprawnienie do grupy',
                'verbose_name_plural': 'Uprawnienia do grup',
            },
        ),
        migrations.CreateModel(
            name='ActionToRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzony')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowany')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Action')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role')),
            ],
            options={
                'verbose_name': 'Uprawnienie do roli',
                'verbose_name_plural': 'Uprawnienia do ról',
            },
        ),
        migrations.AlterUniqueTogether(
            name='actiontorole',
            unique_together={('role', 'action')},
        ),
    ]
