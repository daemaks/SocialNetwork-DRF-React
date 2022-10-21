from core.apps.accounts.models import Account
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import RegisterSerializer, UserSerializer


class CustomCreateAccount(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save()
            if created_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Account.active_objects.all()
    serializer_class = UserSerializer
