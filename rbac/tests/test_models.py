import factory
from django.db import IntegrityError, DataError
from django.test import TestCase

from rbac.tests.factories import RoleFactory


class RoleModelTestCase(TestCase):
    def setUp(self):
        self.role = RoleFactory()

    def test_string_representation(self):
        self.role.name.should.be.eql(str(self.role))

    def test_name(self):
        len(self.role.name).should.be.lower_than(64)

    def test_name_unique(self):
        with self.assertRaises(IntegrityError):
            RoleFactory(name=self.role.name)

    def test_name_too_long(self):
        with self.assertRaises(DataError):
            RoleFactory(name=factory.Faker('text', max_nb_chars=128))

    def test_active_not_null(self):
        with self.assertRaises(IntegrityError):
            RoleFactory(active=None)

    def test_active_is_boolean(self):
        self.role.active.should.be.an(bool)
