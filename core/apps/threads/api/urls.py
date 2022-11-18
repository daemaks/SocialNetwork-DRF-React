from django.urls import path

from . import views

urlpatterns = [
    # Tag
    path(
        "tag/",
        views.TagViewSet.as_view({"get": "list"}),
        name="tag_list",
    ),
    path(
        "tag/<int:pk>/",
        views.TagViewSet.as_view({"get": "retrieve"}),
        name="tag_details",
    ),
    # Communities
    path(
        "community/",
        views.CommunityListView.as_view({"get": "list", "get": "retrieve"}),
        name="community_list",
    ),
    # Threads
    path(
        "community/<int:pk>/threads",
        views.ThreadsViewSet.as_view({"get": "list"}),
        name="threads_list_of_community",
    ),
    path(
        "", views.ThreadsViewSet.as_view({"get": "list"}), name="threads_list"
    ),
    path(
        "<int:pk>/",
        views.ThreadsViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="threads_details",
    ),
    path(
        "create/",
        views.ThreadsViewSet.as_view({"post": "create"}),
        name="threads_create",
    ),
    # Comment
    path(
        "thread/<int:pk>/comments/",
        views.CommentsViewSet.as_view({"get": "list"}),
        name="comments_of_thread",
    ),
    path(
        "comment/<int:pk>/",
        views.CommentsViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="comment_details",
    ),
    path(
        "thread/<int:pk>/likes", views.LikesView.as_view(), name="likes_count"
    ),
]
