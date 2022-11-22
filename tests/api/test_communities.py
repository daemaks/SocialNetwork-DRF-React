import pytest
from rest_framework.test import APIClient
from django.urls import reverse

# client = APIClient()


@pytest.mark.django_db
def test_tag_list(api_tag, client):
    url = reverse("tag_list")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_tag_details(api_community, client):
    url = "http://127.0.0.1:8000/api/threads/tag/1/"
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_community_list(api_community, client):
    url = reverse("community_list")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
