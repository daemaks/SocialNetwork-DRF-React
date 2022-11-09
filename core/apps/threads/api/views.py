from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import (
    CommunitySerializer,
    TagDetailsSerializer,
    TagSerializer,
)


class TagListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailsView(APIView):
    def get(self, request, pk):
        communities = Community.objects.filter(tag=pk)
        serializer = TagDetailsSerializer(communities, many=True)
        return Response(serializer.data)


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
