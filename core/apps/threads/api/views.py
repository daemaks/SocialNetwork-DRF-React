from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import TagSerializer


class TagListViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
