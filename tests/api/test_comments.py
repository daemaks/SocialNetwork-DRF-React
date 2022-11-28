import pytest
from django.urls import reverse
from core.apps.threads.models import Thread, Comment

"""CREATE"""


@pytest.mark.django_db
def test_comment_create(api_account, api_community):

    """test_comment_create"""
    Thread.objects.create(username_id=1, title="example", community_id=1)
    response = api_account.post(
        reverse("comment_create"), {"text": "test", "thread": 1}
    )
    data = response.data
    data_from_db = Comment.objects.all().first()

    assert data["text"] == data_from_db.text
    assert data["thread"] == data_from_db.thread.id
    assert data["username"] == data_from_db.username.id

    """test_comments_list_of_thread"""
    response = api_account.get(
        reverse("comments_of_tread", kwargs={"pk": "1"})
    )

    assert response.status_code == 200

    """test_comments_list_of_thread_404"""
    response = api_account.get(
        reverse("comments_of_tread", kwargs={"pk": "0"})
    )

    assert response.status_code == 404

    """test_comments_retrieve"""
    response = api_account.get(reverse("comment_details", kwargs={"pk": "1"}))

    assert response.status_code == 200


"""UPDATE"""


@pytest.mark.django_db
def test_comments_update_by_owner(api_account, api_comment):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.put(url, {"text": "testtext"})

    assert response.status_code == 200


@pytest.mark.django_db
def test_comments_update_by_other_user(
    api_account, api_account_2, api_comment
):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account_2.put(url, {"text": "testtext"})

    assert response.status_code == 403


@pytest.mark.django_db
def test_comments_update_by_admin(api_account, api_admin_account, api_comment):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_admin_account.put(url, {"text": "testtext"})

    assert response.status_code == 403


"""DESTROY"""


@pytest.mark.django_db
def test_comments_destroy_by_owner(api_account, api_comment):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.delete(url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_comments_destroy_by_other_user(
    api_account, api_account_2, api_comment
):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account_2.delete(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_comments_destroy_by_admin(
    api_account, api_admin_account, api_comment
):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_admin_account.delete(url)

    assert response.status_code == 204
