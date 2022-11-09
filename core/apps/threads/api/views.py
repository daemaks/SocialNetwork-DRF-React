from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import (
    CommentSerializer,
    CommunitySerializer,
    TagDetailsSerializer,
    TagSerializer,
)


class TagViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Community.objects.filter(tag=pk)
        serializer = TagDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommentView(APIView):
    def get(self, request, pk):
        queryset = Comment.objects.filter(thread=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
