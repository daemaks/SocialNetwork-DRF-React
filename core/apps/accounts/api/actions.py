from . import views

register = views.CustomCreateAccountView.as_view()
logout = views.BlacklistTokenView.as_view()
user_list = views.UserViewSet.as_view({"get": "list"})
user_details = views.UserViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
