from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# 🔹 Create router instance
router = DefaultRouter()

# 🔹 Register routes for Post and Comment
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# 🔹 Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]
