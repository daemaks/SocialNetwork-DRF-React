from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from tools.permissions import IsOwnerOrReadOnly

from .serializer import (
    CommentSerializer,
    CommunitySerializer,
    TagDetailsSerializer,
    TagSerializer,
    ThreadSerializer,
)


class TagViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Community.objects.filter(tag=pk)
        serializer = TagDetailsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class ThreadsViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, pk=None):
        if pk:
            queryset = Thread.objects.filter(community=pk)
            serializer = ThreadSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            queryset = Thread.objects.all()
            serializer = ThreadSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Thread.objects.get(pk=pk)
        serializer = ThreadSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass


class CommentsViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, pk):
        queryset = Comment.objects.filter(thread=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass
