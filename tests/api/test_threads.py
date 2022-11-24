import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.apps.threads.models import Thread

client = APIClient()


@pytest.mark.django_db
def test_thread_create(api_account, api_community):
    url = reverse("threads_create")
    payload = {"title": "example", "community": 1}
    response = api_account.post(url, payload)
    data = response.data
    data_from_db = Thread.objects.all().first()

    assert data["id"] == data_from_db.id
    assert data["title"] == data_from_db.title
    assert data["community"] == data_from_db.community.id
    assert data["username"] == data_from_db.username.id


@pytest.mark.django_db
def test_threads_list(db, api_thread):
    url = reverse("treads_list")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_threads_list_of_community(db, api_thread):
    url = reverse("threads_list_of_community", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_threads_details_get_method(api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200
