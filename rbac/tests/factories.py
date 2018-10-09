import factory

from rbac import models


class ActionFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Action

    name = factory.Faker('word')
    codename = factory.LazyAttribute(lambda x: "{0}.{0}.{0}".format(x.name))


class ActionToGroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ActionToGroup

    action = factory.SubFactory('rbac.tests.factories.ActionFactory')
    group = factory.SubFactory('common.factories.GroupFactory')


class ActionToRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ActionToRole

    role = factory.SubFactory('rbac.tests.factories.RoleFactory')
    action = factory.SubFactory('rbac.tests.factories.ActionFactory')


class GroupToRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.GroupToRole

    role = factory.SubFactory('rbac.tests.factories.RoleFactory')
    group = factory.SubFactory('common.factories.GroupFactory')


class RoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Role

    name = factory.Faker('word')
    active = True


class RoleToUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.RoleToUser

    user = factory.SubFactory('common.factories.UserFactory')
    role = factory.SubFactory('rbac.tests.factories.RoleFactory')
