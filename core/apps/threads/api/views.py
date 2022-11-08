from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import CommunitySerializer, TagSerializer


class TagListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
