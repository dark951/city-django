import factory
from django.contrib.auth.models import Group, User


class GroupFactory(factory.DjangoModelFactory):
    """
    Django auth group factory
    """
    class Meta:
        model = Group

    name = factory.Faker('word')


class UserFactory(factory.DjangoModelFactory):
    """
    Django user model factory
    """
    class Meta:
        model = User

    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda x: "user_{0}{1}".format(x.first_name.lower(), x.last_name.lower()))
    email = factory.LazyAttribute(lambda x: "{0}.{1}@localhost.com".format(x.first_name.lower(), x.last_name.lower()))
