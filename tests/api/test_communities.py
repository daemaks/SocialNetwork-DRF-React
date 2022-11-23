import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_tag_list(api_tag, client):
    url = reverse("tag_list")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_tag_details(api_community, client):
    url = reverse("tag_details", kwargs={"pk": "1"})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_community_list(api_community, client):
    url = reverse("community_list")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_community_details(api_community, client):
    url = reverse("community_details", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200
