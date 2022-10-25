from django.urls import path

from .views import CustomCreateAccount, UserViewSet

user_action = UserViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

urlpatterns = [
    # Users Data
    path("", UserViewSet.as_view({"get": "list"}), name="user_list"),
    path("<int:pk>/", user_action, name="user_details"),
    # Registration
    path("register/", CustomCreateAccount.as_view(), name="create_user"),
]
