# Generated by Django 2.1.2 on 2018-10-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rbac', '0002_auto_20181004_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Nazwa'),
        ),
    ]
