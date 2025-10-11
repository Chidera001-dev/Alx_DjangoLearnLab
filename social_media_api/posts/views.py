from rest_framework import viewsets, permissions, filters,generics
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment

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









# Create your views here.
