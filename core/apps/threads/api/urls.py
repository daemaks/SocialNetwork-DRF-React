from django.urls import path

from . import views

urlpatterns = [
    path("tag/", views.TagListView.as_view({"get": "list"}), name="tag_list"),
    path("tag/<int:pk>", views.TagDetailsView.as_view(), name="tag_details"),
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
