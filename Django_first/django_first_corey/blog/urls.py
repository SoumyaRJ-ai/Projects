from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView)
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),  # This is used for executing the view class as views
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Viewing detailed individual views
    # Here we are following the convention we did not follow for the home class view
    # So the idea is like to use \1 for blog1 \2 for blog2 i.e their id's which are the primary keys for them
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]
