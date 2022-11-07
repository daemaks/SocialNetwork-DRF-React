from django.urls import path

from . import views

urlpatterns = [
    path(
        "tag/", views.TagListViewset.as_view({"get": "list"}), name="tag_list"
    ),
]
