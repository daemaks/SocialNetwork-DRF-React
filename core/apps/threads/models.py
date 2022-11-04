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
    members = models.ManyToManyField(
        Account, related_name="Members", blank=True
    )

    class Meta:
        verbose_name = _("Community")
        verbose_name_plural = _("Communities")
        ordering = ["-members"]


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
        Community,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="communities",
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Thread(models.Model):
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
        related_name="author",
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name="community",
    )
    content = models.TextField(
        _("Content"),
        help_text=_("Not requiered. Max length - 500"),
        max_length=500,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Thread")
        verbose_name_plural = _("Threads")
        ordering = ["-created_at"]


class Comment(models.Model):
    author = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="comment",
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="thread",
    )
    text = models.TextField(
        _("Text"),
        help_text=_("Requiered. Max length - 300"),
        max_length=300,
        blank=False,
        null=False,
        unique=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ["-created_at"]


class Likes(models.Model):
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name="thread",
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="user",
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
