import pytest
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()


@pytest.mark.django_db
def test_threads_list(db, api_thread):
    url = reverse("treads_list")
    response = client.get(url)

    assert response.status_code == 200
