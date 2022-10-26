from core.apps.accounts.models import Account
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .serializer import AccountSerializer, RegisterSerializer
from .viewsets import UpgradedModelViewSet


class CustomCreateAccount(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save()
            if created_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(UpgradedModelViewSet):
    permission_classes = [AllowAny]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes_by_action = {
        "update": [IsOwnerOrReadOnly],
        "destroy": [IsOwnerOrReadOnly],
    }
