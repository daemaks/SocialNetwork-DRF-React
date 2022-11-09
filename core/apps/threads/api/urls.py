from django.urls import path

from . import views

urlpatterns = [
    # Tag
    path("tag/", views.TagViewSet.as_view({"get": "list"}), name="tag_list"),
    path(
        "tag/<int:pk>/",
        views.TagViewSet.as_view({"get": "retrieve"}),
        name="tag_details",
    ),
    # Communities
    path(
        "community/",
        views.CommunityListView.as_view({"get": "list"}),
        name="community_list",
    ),
    path(
        "community/<int:pk>/",
        views.CommunityListView.as_view({"get": "retrieve"}),
        name="community_details",
    ),
]
