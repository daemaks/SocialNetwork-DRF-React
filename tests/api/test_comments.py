import pytest
from django.urls import reverse
from core.apps.threads.models import Thread, Comment

"""CREATE"""


@pytest.mark.django_db
def test_comment_create(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    url = reverse("comment_create")
    response = api_account.post(url, {"text": "test", "thread": 1})
    data = response.data
    data_from_db = Comment.objects.all().first()

    assert data["text"] == data_from_db.text
    assert data["thread"] == data_from_db.thread.id
    assert data["username"] == data_from_db.username.id


"""LIST"""


@pytest.mark.django_db
def test_comments_list_of_thread(api_account, api_comment):
    url = reverse("comments_of_tread", kwargs={"pk": "1"})
    response = api_account.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comments_list_of_thread_404(api_account):
    url = reverse("comments_of_tread", kwargs={"pk": "0"})
    response = api_account.get(url)

    assert response.status_code == 404


"""RETRIEVE"""


@pytest.mark.django_db
def test_comments_retrieve(api_account, api_comment):
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.get(url)

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
