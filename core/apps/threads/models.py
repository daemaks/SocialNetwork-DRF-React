from core.apps.accounts.models import Account
from django.db import models
from django.utils.translation import gettext_lazy as _


class Community(models.Model):
    title = models.CharField(
        _("Title"),
        help_text=_("Requiered. Max Length - 30"),
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )
    description = models.CharField(
        _("Description"),
        help_text=_("Not requiered. Max Length - 200"),
        max_length=200,
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(Account)

    class Meta:
        pass


class Tag(models.Model):
    title = models.CharField(
        _("Title"),
        help_text=_("Requiered. Max Length - 30"),
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )
    communities = models.ForeignKey(
        Community, on_delete=models.PROTECT, blank=True, null=True
    )

    class Meta:
        pass


class Threard(models.Model):
    title = models.CharField(
        _("Title"),
        help_text=_("Not requiered. Max Length - 150"),
        max_length=150,
        unique=False,
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        unique=False,
    )
    content = models.TextField(
        _("Content"),
        help_text=_("Not requiered. Max length - 500"),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass


class Comment(models.Model):
    pass

    class Meta:
        pass


class Likes(models.Model):
    pass

    class Meta:
        pass
