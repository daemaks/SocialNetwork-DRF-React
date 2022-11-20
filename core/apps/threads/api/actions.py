from . import views

tag_list = views.TagViewSet.as_view({"get": "list"})
tag_details = views.TagViewSet.as_view({"get": "retrieve"})
community_list = views.CommunityListView.as_view({"get": "list"})
community_details = views.CommunityListView.as_view({"get": "retrieve"})
treads_list = views.ThreadsViewSet.as_view({"get": "list"})
threads_list_of_community = views.ThreadsViewSet.as_view({"get": "list"})
threads_details = views.ThreadsViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
threads_create = views.ThreadsViewSet.as_view({"post": "create"})
comments_of_tread = views.CommentsViewSet.as_view({"get": "list"})
comment_details = views.CommentsViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
comment_create = views.CommentsViewSet.as_view({"post": "create"})
likes = views.LikesView.as_view()
