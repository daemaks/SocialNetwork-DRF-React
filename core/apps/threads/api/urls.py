from django.urls import path, include
from rest_framework import routers
from . import actions
from . import views

router = routers.DefaultRouter()
router.register(r"thread", views.ThreadsViewSet, basename="threads")
print(router.urls)

urlpatterns = [
    # Tag
    path("tag/", actions.tag_list, name="tag_list"),
    path("tag/<int:pk>/", actions.tag_details, name="tag_details"),
    # Communities
    path("community/", actions.community_list, name="community_list"),
    path(
        "community/<slug:slug>",
        actions.community_details,
        name="community_details",
    ),
    # Threads
    path("", include(router.urls)),
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
