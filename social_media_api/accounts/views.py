from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

User = get_user_model()


#  Registration View
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # create token for the new user
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": ProfileSerializer(user).data
        }, status=status.HTTP_201_CREATED)


#  Login View
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "user": ProfileSerializer(user).data
        }, status=status.HTTP_200_OK)


#  Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Create your views here.
