from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from tools.permissions import IsOwnerOrReadOnly

from .serializer import (
    CommentSerializer,
    CommunitySerializer,
    TagDetailsSerializer,
    TagSerializer,
    ThreadSerializer,
    CreateThreadSerializer,
    CreateCommentSerializer,
)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.action == "list":
            return Tag.objects.all()
        elif self.action == "retrieve":
            return Community.objects.filter(tag=self.kwargs["pk"])

    def get_serializer_class(self):
        if self.action == "list":
            return TagSerializer
        elif self.action == "retrieve":
            return TagDetailsSerializer


class CommunityListView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class ThreadsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ThreadSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            return Thread.objects.filter(pk=self.kwargs["pk"])
        elif self.action == "list" and "pk" in self.kwargs:
            return Thread.objects.filter(community=self.kwargs["pk"])
        return Thread.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateThreadSerializer
        return CommentSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.action == "list":
            return Comment.objects.filter(thread=self.kwargs["pk"])
        return Comment.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateCommentSerializer
        return ThreadSerializer


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
