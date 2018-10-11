import os

import yaml
from django.conf import settings
from django.core.management import BaseCommand

from rbac.utils import PrivilegeParser


class Command(BaseCommand):
    help = 'Command collect all permissions from apps placed in installed apps in settings file'

    def handle(self, *args, **options):
        parser = self._get_parser()
        parser.clear()
        for data in self._get_permissions_object():
            parser.parse(data.get('permissions', []))
        parser.propagate()

    @staticmethod
    def _get_permissions_object():
        apps = settings.INSTALLED_APPS
        for app in apps:
            try:
                with open(os.path.join(settings.BASE_DIR, app, 'permissions.yaml'), 'r') as file:
                    yield yaml.load(file)
            except FileNotFoundError:
                continue

    def _get_parser(self):
        if not hasattr(self, 'parser'):
            self.parser = PrivilegeParser()
        return self.parser
