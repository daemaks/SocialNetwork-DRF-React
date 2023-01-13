from django.urls import path

from . import actions

urlpatterns = [
    # Users Data
    path("", actions.user_list, name="user_list"),
    path("<slug:slug>/", actions.user_details, name="user_details"),
    # Registration
    path("register/", actions.register, name="create_user"),
    # Logout
    path("logout/", actions.logout, name="logout"),
]
