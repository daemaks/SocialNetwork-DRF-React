import pytest
from django.urls import reverse
from core.apps.threads.models import Thread, Likes


@pytest.mark.django_db
def test_thread_create_and_safe_requests(api_account, api_community, client):

    """test_thread_create"""
    response = api_account.post(
        reverse("threads_create"), {"title": "example", "community": 1}
    )
    data = response.data
    data_from_db = Thread.objects.all().first()

    assert data["id"] == data_from_db.id
    assert data["title"] == data_from_db.title
    assert data["community"] == data_from_db.community.id
    assert data["username"] == data_from_db.username.id

    """test_threads_list"""
    response = client.get(reverse("treads_list"))

    assert response.status_code == 200

    """test_threads_list_of_community"""
    response = client.get(
        reverse("threads_list_of_community", kwargs={"pk": "1"})
    )

    assert response.status_code == 200

    """test_threads_list_of_community_404"""
    response = client.get(
        reverse("threads_list_of_community", kwargs={"pk": "0"})
    )

    assert response.status_code == 404

    """test_threads_retrieve"""
    response = client.get(reverse("threads_details", kwargs={"pk": "1"}))

    assert response.status_code == 200

    """test_threads_retrieve_404"""
    response = client.get(reverse("threads_details", kwargs={"pk": "0"}))

    assert response.status_code == 404


"""UPDATE"""


@pytest.mark.django_db
def test_thread_update_by_owner(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    url = reverse("threads_details", kwargs={"pk": "1"})
    payload = {"title": "test example"}
    response = api_account.put(url, payload)

    assert response.status_code == 200


@pytest.mark.django_db
def test_thread_update_by_other_user(api_account_2, api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    payload = {"title": "test example"}
    response = api_account_2.put(url, payload)

    assert response.status_code == 403


@pytest.mark.django_db
def test_thread_update_by_admin(api_admin_account, api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    payload = {"title": "test example"}
    response = api_admin_account.put(url, payload)

    assert response.status_code == 403


"""DESTROY"""


@pytest.mark.django_db
def test_thread_destroy_by_owner(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = api_account.delete(url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_thread_delete_by_other_user(api_account_2, api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = api_account_2.delete(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_thread_destroy_by_admin(api_admin_account, api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = api_admin_account.delete(url)

    assert response.status_code == 204


"""LIKE"""


@pytest.mark.django_db
def test_thread_likes_count(client, api_thread):
    url = reverse("likes", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200


def test_thread_post_like(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    url = reverse("likes", kwargs={"pk": "1"})
    api_account.post(url)
    assert Likes.objects.filter(thread=1).count() == 1
    api_account.post(url)
    assert Likes.objects.filter(thread=1).count() == 0
