# blog/URLs
from django.urls import path
from .views import home, about, create_post, post_detail
from .views import (PostListView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView
                    )
urlpatterns = [
    #path('', home, name='home'),
    #path('comment/', comment_view, name='comment'),
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', about, name='about'),

]
