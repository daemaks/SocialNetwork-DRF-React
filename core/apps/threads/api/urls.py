from django.urls import path
from . import actions

urlpatterns = [
    # Tag
    path("tag/", actions.tag_list, name="tag_list"),
    path("tag/<int:pk>/", actions.tag_details, name="tag_details"),
    # Communities
    path("community/", actions.community_list, name="community_list"),
    path(
        "community/<int:pk>",
        actions.community_details,
        name="community_details",
    ),
    # Threads
    path(
        "community/<int:pk>/threads",
        actions.threads_list_of_community,
        name="threads_list_of_community",
    ),
    path("", actions.treads_list, name="treads_list"),
    path("<int:pk>/", actions.threads_details, name="threads_details"),
    path("create/", actions.threads_create, name="threads_create"),
    # Comment
    path(
        "thread/<int:pk>/comments/",
        actions.comments_of_tread,
        name="comments_of_tread",
    ),
    path("comment/<int:pk>/", actions.comment_details, name="comment_details"),
    path("comment/create/", actions.comment_create, name="comment_create"),
    # Likes
    path("thread/<int:pk>/likes", actions.likes, name="likes"),
]
