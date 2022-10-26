from .views import CustomCreateAccount, UserViewSet

register = CustomCreateAccount.as_view()
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
