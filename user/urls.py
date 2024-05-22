from user.views import UserPostView
from django.urls import path

urlpatterns = [
    path('posts/', UserPostView.as_view(), name='user_posts'),
]