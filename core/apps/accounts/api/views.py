from core.apps.accounts.models import Account
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from tools.permissions import IsOwnerOrReadOnly

from .serializer import AccountSerializer, RegisterSerializer


# Register
class CustomCreateAccountView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save()
            if created_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Logout
class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
