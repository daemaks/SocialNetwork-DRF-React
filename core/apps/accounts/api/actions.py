from .views import BlacklistTokenView, CustomCreateAccountView, UserViewSet

register = CustomCreateAccountView.as_view()
logout = BlacklistTokenView.as_view()
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
