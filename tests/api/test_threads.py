import pytest
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()


@pytest.mark.django_db
def test_threads_list(db, api_thread):
    url = reverse("treads_list")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_threads_list_of_community(db, api_thread):
    url = reverse("threads_list_of_community", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200
