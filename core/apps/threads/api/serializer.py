from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import serializers


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
