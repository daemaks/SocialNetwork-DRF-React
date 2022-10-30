import pytest
from pytest_factoryboy import register

from .factory import AccountsFactory

register(AccountsFactory)


@pytest.fixture
def account(db, accounts_factory):
    user = accounts_factory.create()
    return user


@pytest.fixture
def admin_user_base(db, accounts_factory):
    user = accounts_factory.create(
        name="admin_user", is_staff=True, is_superuser=True
    )
    return user
