import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    url = reverse("create_user")
    response = client.post(url, payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_register_user_fail():
    payload = {
        "username": "example",
        "password": "example",
    }
    url = reverse("create_user")
    response = client.post(url, payload)

    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user(account):
    url = reverse("token_obtain_pair")

    response = client.post(
        url,
        {"email": "example@test.com", "password": "testtest"},
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(account):
    url = reverse("token_obtain_pair")

    response = client.post(
        url,
        {"email": "test@test.com", "password": "testtest"},
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_change_user_data(api_account):
    url = "http://127.0.0.1:8000/api/user/1/"
    response = api_account.put(url, {"username": "tester"})
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_other_user_data(api_account):
    url = "http://127.0.0.1:8000/api/user/2/"
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    client.post(reverse("create_user"), payload)
    response = api_account.put(url, {"username": "tester"})

    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_user_data(api_account):
    url = "http://127.0.0.1:8000/api/user/1/"
    response = api_account.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_other_user_data(api_account):
    url = "http://127.0.0.1:8000/api/user/2/"
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    client.post(reverse("create_user"), payload)
    response = api_account.delete(url)

    assert response.status_code == 403
