from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils.translation import gettext_lazy as _
from tools.validators import validate_image


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")

        if other_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must be assigned to is_superuser=True."
            )

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_("Users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=60, unique=True)
    username = models.CharField(_("Username"), max_length=100, unique=True)
    avatar = models.ImageField(
        _("Avatar"),
        upload_to="avatar/",
        blank=True,
        null=True,
        validators=[validate_image, validate_image_file_extension],
        help_text=("Not required. Maximum file size allowed is 2Mb"),
    )
    about = models.TextField(_("About"), max_length=150, blank=True)
    date_joined = models.DateTimeField(_("Joined Date"), auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
