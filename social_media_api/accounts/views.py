from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated  
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Post
from .serializers import PostSerializer

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
    


# 🔹 Follow another user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(target_user)
        return Response({"message": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


# 🔹 Unfollow another user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if target_user == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(target_user)
        return Response({"message": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)


class FeedView(generics.GenericAPIView):
    """
    Returns posts from users the current user follows.
    Ordered by most recent first.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        # Get all users that the logged-in user follows
        following_users = request.user.following.all()

        # Get posts made by those users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)        

# Create your views here.
