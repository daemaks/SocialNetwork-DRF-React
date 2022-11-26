import pytest
from django.urls import reverse
from core.apps.threads.models import Thread, Comment

"""LIST"""


@pytest.mark.django_db
def test_comments_list_of_thread(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comments_of_tread", kwargs={"pk": "1"})
    response = api_account.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comments_retrieve(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.get(url)

    assert response.status_code == 200


"""UPDATE"""


@pytest.mark.django_db
def test_comments_update_by_owner(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.put(url, {"text": "testtext"})

    assert response.status_code == 200


@pytest.mark.django_db
def test_comments_update_by_other_user(
    api_account, api_account_2, api_community
):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account_2.put(url, {"text": "testtext"})

    assert response.status_code == 403


@pytest.mark.django_db
def test_comments_update_by_admin(
    api_account, api_admin_account, api_community
):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_admin_account.put(url, {"text": "testtext"})

    assert response.status_code == 403


"""DESTROY"""


@pytest.mark.django_db
def test_comments_destroy_by_owner(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.delete(url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_comments_destroy_by_other_user(
    api_account, api_account_2, api_community
):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account_2.delete(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_comments_destroy_by_admin(
    api_account, api_admin_account, api_community
):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_admin_account.delete(url)

    assert response.status_code == 204
