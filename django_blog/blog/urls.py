from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("profile/", views.profile, name="profile"),


  path('post/', PostListView.as_view(), name='post-list'),                  # List all posts
path('post/new/', PostCreateView.as_view(), name='post-create'),          # Create a new post
path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),     # View post detail
path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),# Edit a post
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete a post

]