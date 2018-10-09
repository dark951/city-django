from rbac.models import PermissionUpload


class PrivilegeParser(object):
    """
    Parser for privileges data object retrieved from privileges files located in apps directory
    """

    def parse_data(self, data):
        # simplify structure, built up on generator syntax
        # bull insert data
        self._insert_data(data)

    def _simplify_structure(self, data):
        pass

    def _insert_data(self, data):
        PermissionUpload.objects.bulk_create([PermissionUpload(**row) for row in data])
