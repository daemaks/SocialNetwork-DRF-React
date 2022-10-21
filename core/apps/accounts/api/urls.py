from django.urls import path

from .views import CustomCreateAccount

urlpatterns = [
    # Registration
    path("register/", CustomCreateAccount.as_view(), name="create_user")
]
