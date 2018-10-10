from rbac.models import PermissionUpload


class PrivilegeParser(object):
    """
    Parser for privileges data object retrieved from privileges files located in apps directory
    """
    @staticmethod
    def clear():
        PermissionUpload.clear()

    def parse(self, data):
        # simplify structure and next insert it in data base
        self._insert_data(list(self._simplify_structure(data, None)))

    def _simplify_structure(self, data, group):
        # simplify structure, build up on generator syntax with recursion
        for row in data:
            if 'permissions' in row:
                for i_row in self._simplify_structure(row.get('permissions', []), row.get('name')):
                    yield i_row
            else:
                yield {'name': row.get('name'), 'codename': row.get('permission'), 'group': group}

    @staticmethod
    def _insert_data(data):
        PermissionUpload.objects.bulk_create([PermissionUpload(**row) for row in data])
