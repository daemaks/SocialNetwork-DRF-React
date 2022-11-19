from django.urls import path
from . import actions

urlpatterns = [
    # Tag
    path(
        "tag/",
        actions.tag_list,
    ),
    path(
        "tag/<int:pk>/",
        actions.tag_details,
    ),
    # Communities
    path(
        "community/",
        actions.community_list,
    ),
    path(
        "community/<int:pk>",
        actions.community_details,
    ),
    # Threads
    path(
        "community/<int:pk>/threads",
        actions.threads_list_of_community,
    ),
    path(
        "",
        actions.treads_list,
    ),
    path(
        "<int:pk>/",
        actions.threads_details,
    ),
    path(
        "create/",
        actions.threads_create,
    ),
    # Comment
    path(
        "thread/<int:pk>/comments/",
        actions.comments_of_tread,
    ),
    path(
        "comment/<int:pk>/",
        actions.comment_details,
    ),
    ##Create Comment!!!
    # Likes
    path("thread/<int:pk>/likes", actions.likes),
]
