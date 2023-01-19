import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_community_requests(api_community, client):

    """test_tag_list"""
    response = client.get(reverse("tag_list"))

    assert response.status_code == 200

    """test_tag_details"""
    response = client.get(reverse("tag_details", kwargs={"pk": "1"}))
    assert response.status_code == 200

    """test_community_list"""
    response = client.get(reverse("community_list"))

    assert response.status_code == 200

    """test_community_details"""
    response = client.get(
        reverse("community_details", kwargs={"slug": "comtest"})
    )

    assert response.status_code == 200
