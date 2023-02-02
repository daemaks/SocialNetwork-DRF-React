from rest_framework import serializers

from core.apps.threads.models import Comment, Community, Tag, Thread
from core.apps.accounts.api.serializer import AccountSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CommunitySerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Community
        fields = "__all__"


class ThreadSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Thread
        fields = "__all__"
        read_only_fields = ["community"]

        depth = 1


class CreateThreadSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Thread
        fields = "__all__"

    def create(self, validated_data):
        if "username" not in validated_data:
            validated_data["username"] = self.context["request"].user

        return Thread.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    username = AccountSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["thread"]


class CreateCommentSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        if "username" not in validated_data:
            validated_data["username"] = self.context["request"].user

        return Comment.objects.create(**validated_data)
