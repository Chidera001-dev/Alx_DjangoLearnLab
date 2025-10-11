from rest_framework import viewsets, permissions, filters,generics, status
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from rest_framework.response import Response 
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from .models import Post, Like
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, CommentSerializer

User = get_user_model()


# 🔹 Custom Permission: Only owner can edit/delete
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# 🔹 Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5                     
    page_size_query_param = 'page_size'
    max_page_size = 50


# 🔹 Post ViewSet
class PostViewSet(viewsets.ModelViewSet):  
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    #  Filtering and Searching
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# 🔹 Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):   
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        user = request.user
        
        following_users = user.following.all()

        
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)        


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Optionally create notification
        # Notification.objects.create(
        #     recipient=post.author,
        #     actor=request.user,
        #     verb="liked your post",
        #     target=post
        # )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)