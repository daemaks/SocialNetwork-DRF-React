import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .factory import AccountsFactory, TagFactory, CommunityFactory

register(AccountsFactory)
register(TagFactory)
register(CommunityFactory)

# Account Fixture
@pytest.fixture
def account(db, accounts_factory):
    user = accounts_factory.create()
    return user


@pytest.fixture
def admin_account(db, accounts_factory):
    user = accounts_factory.create(
        name="admin_user", is_staff=True, is_superuser=True
    )
    return user


@pytest.fixture
def api_account(db, accounts_factory):
    user = accounts_factory.create()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def api_admin_account(db, accounts_factory):
    user = accounts_factory.create(is_staff=True)
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


# Threads Fixture
@pytest.fixture
def tag(db, tag_factory):
    data = tag_factory.create()
    return data


# @pytest.fixture
# def comunity
