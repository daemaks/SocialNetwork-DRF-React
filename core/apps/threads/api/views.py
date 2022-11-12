from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from rest_framework import viewsets
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
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk):
        queryset = Community.objects.filter(tag=pk)
        serializer = TagDetailsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


# class CommentView(APIView):
#     permission_classes = [IsOwnerOrReadOnly]

#     def get(self, request, pk):
#         queryset = Comment.objects.filter(thread=pk)
#         serializer = CommentSerializer(queryset, many=True)
#         return Response(serializer.data)


class CommentsViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, pk):
        queryset = Comment.objects.filter(thread=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk):
        queryset = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


class ThreadsViewSet(viewsets.ViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request, pk=None):
        if pk:
            queryset = Thread.objects.filter(community=pk)
            serializer = ThreadSerializer(queryset, many=True)
            return Response(serializer.data, status=200)
        else:
            queryset = Thread.objects.all()
            serializer = ThreadSerializer(queryset, many=True)
            return Response(serializer.data, status=200)
