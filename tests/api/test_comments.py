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


@pytest.mark.django_db
def test_comments_update(api_account, api_community):
    Thread.objects.create(username_id=1, title="example", community_id=1)
    Comment.objects.create(username_id=1, thread_id=1, text="example")
    url = reverse("comment_details", kwargs={"pk": "1"})
    response = api_account.put(url, {"text": "testtext"})

    assert response.status_code == 200
