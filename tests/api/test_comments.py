import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.apps.threads.models import Comment

client = APIClient()


"""LIST"""


@pytest.mark.django_db
def test_comments_list_of_thread(api_thread):
    url = reverse("comments_of_tread", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200


"""RETRIEVE"""
