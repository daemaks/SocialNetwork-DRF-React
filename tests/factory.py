from core.apps.accounts.models import Account
from core.apps.threads.models import Tag, Community, Thread

from faker import Faker
import factory

fake = Faker()

# Account


class AccountsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    email = "example@test.com"
    username = "user_test"
    password = "testtest"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    title = "Test"


class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Community

    title = "Test Community"
    slug = "comtest"
    description = fake.text()
    tag = factory.SubFactory(TagFactory)


class ThreadsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Thread

    title = "Test Thread"
    username = factory.SubFactory(AccountsFactory)
    community = factory.SubFactory(CommunityFactory)
    content = fake.text()
