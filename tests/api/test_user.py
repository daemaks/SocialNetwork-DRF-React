from http import client

import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    response = client.post("http://127.0.0.1:8000/api/user/register/", payload)

    assert response.status_code == 201


@pytest.mark.django_db
def test_register_user_fail():
    payload = {
        "username": "example",
        "password": "example",
    }
    response = client.post("http://127.0.0.1:8000/api/user/register/", payload)

    assert response.status_code == 400


@pytest.mark.django_db
def test_login_user():
    payload = {
        "email": "example@mail.com",
        "username": "example",
        "password": "example",
    }
    client.post("http://127.0.0.1:8000/api/user/register/", payload)

    response = client.post(
        "http://127.0.0.1:8000/api/token/",
        {"email": "example@mail.com", "password": "example"},
    )

    assert response.status_code == 200
