from core.apps.accounts.models import Account

import factory

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
