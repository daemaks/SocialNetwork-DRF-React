from rest_framework import serializers

from core.apps.threads.models import Comment, Community, Likes, Tag, Thread


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ["id", "title"]


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"


class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Thread
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = "__all__"
