import factory
from django.db import IntegrityError, DataError
from django.test import TestCase

from rbac import models
from rbac.tests.factories import RoleFactory, ActionFactory, ActionToRoleFactory, ActionToGroupFactory


class ActionTestCase(TestCase):
    def setUp(self):
        self.action = ActionFactory()

    def test_creation(self):
        self.action.should.be.an(models.Action)

    def test_string_representation(self):
        "{0}({1})".format(self.action.name, self.action.codename).should.be.eql(str(self.action))

    def test_name(self):
        len(self.action.name).should.be.lower_than(64)

    def test_name_to_long(self):
        with self.assertRaises(DataError):
            ActionFactory(name=factory.Faker('text', max_nb_chars=70))

    def test_codename(self):
        len(self.action.codename).should.be.lower_than(100)

    def test_codename_to_long(self):
        with self.assertRaises(DataError):
            ActionFactory(codename=factory.Faker('text', max_nb_chars=200))

    def test_unique(self):
        with self.assertRaises(IntegrityError):
            ActionFactory(name=self.action.name, codename=self.action.codename)


class ActionToRoleTestCase(TestCase):
    def setUp(self):
        self.action_to_role = ActionToRoleFactory()

    def test_creation(self):
        self.action_to_role.should.be.an(models.ActionToRole)

    def test_uniques(self):
        with self.assertRaises(IntegrityError):
            ActionToRoleFactory(role=self.action_to_role.role, action=self.action_to_role.action)

    def test_action_requiration(self):
        with self.assertRaises(IntegrityError):
            ActionToRoleFactory(action=None)

    def test_role_requiration(self):
        with self.assertRaises(IntegrityError):
            ActionToRoleFactory(role=None)

    def test_representation(self):
        str(self.action_to_role).should.be.equal(
            "{0}[{1}]".format(str(self.action_to_role.action), str(self.action_to_role.role)))


class ActionToGroupTestCase(TestCase):
    def setUp(self):
        self.action_to_group = ActionToGroupFactory()

    def test_creation(self):
        self.action_to_group.should.be.an(models.ActionToGroup)

    def test_uniques(self):
        with self.assertRaises(IntegrityError):
            ActionToGroupFactory(group=self.action_to_group.group, action=self.action_to_group.action)

    def test_action_requiration(self):
        with self.assertRaises(IntegrityError):
            ActionToGroupFactory(action=None)

    def test_groupy_requiration(self):
        with self.assertRaises(IntegrityError):
            ActionToGroupFactory(group=None)

    def test_representation(self):
        str(self.action_to_group).should.be.eql(
            "{0}[{1}]".format(str(self.action_to_group.action), str(self.action_to_group.group)))


class GroupToRoleTestCase(TestCase):
    pass


class RoleModelTestCase(TestCase):
    """
    Role model test
    """

    def setUp(self):
        self.role = RoleFactory()

    def test_creation(self):
        self.role.should.be.an(models.Role)

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

    def test_name_requiration(self):
        with self.assertRaises(IntegrityError):
            RoleFactory(name=None)

    def test_active_not_null(self):
        with self.assertRaises(IntegrityError):
            RoleFactory(active=None)

    def test_active_is_boolean(self):
        self.role.active.should.be.an(bool)
