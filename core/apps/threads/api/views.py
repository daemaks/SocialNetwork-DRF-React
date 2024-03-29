from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404

from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from tools.permissions import IsOwnerOrReadOnly

from .serializer import (
    CommentSerializer,
    CommunitySerializer,
    TagSerializer,
    ThreadSerializer,
    CreateThreadSerializer,
    CreateCommentSerializer,
)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def retrieve(self, request, pk):
        communities = get_list_or_404(Community, tag=pk)
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    lookup_field = "slug"


class ThreadsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Thread.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateThreadSerializer
        return ThreadSerializer

    @action(methods=["get"], detail=True)
    def community_threads(self, request, pk):
        threads = get_list_or_404(Thread, community__slug__contains=pk)
        return Response(
            ThreadSerializer(threads, many=True).data,
            status=status.HTTP_200_OK,
        )

    @action(methods=["get"], detail=True)
    def user_threads(self, request, pk):
        threads = get_list_or_404(Thread, username__slug__contains=pk)
        return Response(
            ThreadSerializer(threads, many=True).data,
            status=status.HTTP_200_OK,
        )


class CommentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.action == "list":
            comments = get_list_or_404(Comment, thread=self.kwargs["pk"])
            return comments
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateCommentSerializer
        return CommentSerializer


class LikesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        likes = Likes.objects.filter(thread=pk).count()
        return Response(likes, status=status.HTTP_200_OK)

    def post(self, request, pk):
        try:
            Likes.objects.get(thread=pk, user=request.user).delete()
        except:
            thread = Thread.objects.get(pk=pk)
            Likes.objects.create(thread=thread, user=request.user)
        likes = Likes.objects.filter(thread=pk).count()
        return Response(likes)
