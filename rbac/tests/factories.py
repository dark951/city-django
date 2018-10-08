import factory

from rbac import models


class ActionFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Action

    name = factory.Faker('word')
    codename = factory.LazyFunction(lambda x: "{0}.{0}.{0}".format(x.name))


class ActionToRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ActionToRole

    role_id = factory.SubFactory('rbac.tests.factories.RoleFactory')
    action_id = factory.SubFactory('rbac.tests.factories.ActionFactory')


class RoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Role

    name = factory.Faker('word')
    active = True
