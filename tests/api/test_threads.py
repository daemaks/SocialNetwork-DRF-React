import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core.apps.threads.models import Thread

client = APIClient()

"""CREATE"""


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


"""LIST"""


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


"""RETRIEVE"""


@pytest.mark.django_db
def test_threads_retrieve(api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_threads_retrieve_404():
    url = reverse("threads_details", kwargs={"pk": "0"})
    response = client.get(url)

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
def test_thread_update_by_other_user(api_thread, api_account_2):
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
def test_thread_delete_by_other_user(api_thread, api_account_2):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = api_account_2.delete(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_thread_destroy_by_admin(api_admin_account, api_thread):
    url = reverse("threads_details", kwargs={"pk": "1"})
    response = api_admin_account.delete(url)

    assert response.status_code == 204
