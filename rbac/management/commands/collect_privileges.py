import os

import yaml
from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Command collect all permissions from apps placed in installed apps in settings file'

    def handle(self, *args, **options):
        for data in self._get_permissions_object():
            print(data)

    def _get_permissions_object(self):
        apps = settings.INSTALLED_APPS
        for app in apps:
            try:
                with open(os.path.join(settings.BASE_DIR, app, 'permissions.yaml'), 'r') as file:
                    yield yaml.load(file)
            except FileNotFoundError:
                continue
