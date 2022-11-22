import pytest
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()


@pytest.mark.django_db
def test_tag_list(tag):
    url = reverse("tag_list")
    responce = client.get(url)

    assert responce.status_code == 200
    assert len(responce.data) == 1
