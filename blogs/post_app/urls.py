from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, PostUpdateView, PostDeletelView, userpost, Likeview

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/Update_post/<int:pk>', PostUpdateView.as_view(),name='edit_post'),
    path('article/delete/<int:pk>', PostDeletelView.as_view(), name='delete_post'),
    path('mypost/<int:pk>', userpost, name='mypost'),
    path('like/<int:pk>', Likeview, name='like_post'),
]
