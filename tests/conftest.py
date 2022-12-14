import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.apps.threads.models import Thread, Comment

from .factory import (
    AccountsFactory,
    TagFactory,
    CommunityFactory,
    ThreadsFactory,
)

register(AccountsFactory)
register(TagFactory)
register(CommunityFactory)
register(ThreadsFactory)


@pytest.fixture
def client():
    return APIClient()


"""Account Fixture"""


@pytest.fixture
def api_account(db, accounts_factory, client):
    user = accounts_factory.create()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def api_account_2(db, accounts_factory, client):
    user = accounts_factory.create(
        username="jestertester",
        email="jestertester@mail.com",
        password="jestertester",
    )
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def api_admin_account(db, accounts_factory, client):
    user = accounts_factory.create(
        is_staff=True,
        username="admintester",
        email="admintester@mail.com",
        password="admintester",
    )
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


"""Threads Fixture"""


@pytest.fixture
def api_tag(db, tag_factory):
    return tag_factory.create()


@pytest.fixture
def api_community(db, community_factory):
    return community_factory.create()


@pytest.fixture
def api_thread(db, threads_factory):
    return threads_factory.create()


@pytest.fixture
def api_comment(db, api_community):
    thread = Thread.objects.create(
        username_id=1, title="example", community_id=1
    )
    comment = Comment.objects.create(
        username_id=1, thread_id=1, text="example"
    )
    return thread, comment
