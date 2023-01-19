import pytest
from django.urls import reverse
from core.apps.accounts.models import Account


"""CREATE"""


@pytest.mark.django_db
def test_register_user(client):
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    url = reverse("create_user")
    response = client.post(url, payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_register_user_fail(client):
    payload = {
        "username": "example",
        "password": "example",
    }
    url = reverse("create_user")
    response = client.post(url, payload)

    assert response.status_code == 400


"""LOGIN"""


@pytest.mark.django_db
def test_login_user(api_account, client):
    url = reverse("token_obtain_pair")

    response = client.post(
        url,
        {"email": "example@test.com", "password": "testtest"},
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(api_account, client):
    url = reverse("token_obtain_pair")

    response = client.post(
        url,
        {"email": "test@test.com", "password": "testtest"},
    )

    assert response.status_code == 401


"""RETRIEVE"""


@pytest.mark.django_db
def test_user_retrieve(api_account):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_account.get(url)
    data = response.data
    data_from_db = Account.objects.all().first()

    assert response.status_code == 200

    assert data["id"] == data_from_db.id
    assert data["username"] == data_from_db.username


"""UPDATE"""


@pytest.mark.django_db
def test_user_update_by_owner(api_account):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_account.put(url, {"username": "tester"})
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_update_by_other_user(api_account, api_account_2):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_account_2.put(url, {"username": "tester"})

    assert response.status_code == 403


@pytest.mark.django_db
def test_user_update_by_admin(api_account, api_admin_account):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_admin_account.put(url, {"username": "tester"})

    assert response.status_code == 403


"""DESTROY"""


@pytest.mark.django_db
def test_user_destroy_by_owner(api_account):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_account.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_user_destroy_by_other_user(api_account, api_account_2):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_account_2.delete(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_user_destroy_by_admin(api_account, api_admin_account):
    url = reverse("user_details", kwargs={"slug": "user_test"})
    response = api_admin_account.delete(url)

    assert response.status_code == 204
