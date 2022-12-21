from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.accounts.models import Account

from tools.validators import validate_image


class Tag(models.Model):
    title = models.CharField(
        _("Title"),
        help_text=_("Requiered. Max Length - 30"),
        max_length=30,
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


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
        help_text=_("Not requiered. Max Length - 100"),
        max_length=100,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _("Community picture"),
        upload_to="community_picture/",
        blank=True,
        null=True,
        validators=[validate_image, validate_image_file_extension],
        help_text=("Not required. Maximum file size allowed is 2Mb"),
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    members = models.ManyToManyField(
        Account,
        blank=True,
    )

    class Meta:
        verbose_name = _("Community")
        verbose_name_plural = _("Communities")

    def __str__(self):
        return self.title


class Thread(models.Model):
    title = models.CharField(
        _("Title"),
        help_text=_("Not requiered. Max Length - 150"),
        max_length=150,
        unique=False,
        blank=False,
        null=False,
    )
    username = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )
    content = models.TextField(
        _("Content"),
        help_text=_("Not requiered. Max length - 200"),
        max_length=200,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _("Thread picture"),
        upload_to="thread_picture/",
        blank=True,
        null=True,
        validators=[validate_image, validate_image_file_extension],
        help_text=("Not required. Maximum file size allowed is 2Mb"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Thread")
        verbose_name_plural = _("Threads")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    text = models.TextField(
        _("Text"),
        help_text=_("Requiered. Max length - 150"),
        max_length=150,
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
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
