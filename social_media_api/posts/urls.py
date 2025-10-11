from django.urls import path
from . import views

urlpatterns = [
    # ---- POSTS ----
    path("posts/", views.PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),

    # ---- COMMENTS ----
    path("comments/", views.CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", views.CommentDetailView.as_view(), name="comment-detail"),
]
