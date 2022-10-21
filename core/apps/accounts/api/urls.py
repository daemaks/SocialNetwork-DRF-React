from django.urls import path

from .views import CustomCreateAccount, UserList  # UserDetails,

urlpatterns = [
    # Users Data
    path("", UserList.as_view(), name="user_list"),
    # path("<str:username>/", UserDetails.as_view(), name="user_details"),
    # Registration
    path("register/", CustomCreateAccount.as_view(), name="create_user"),
]
