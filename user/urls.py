from user.views import UserPostView, OwnUserDetailView, PublicUserDetailView, DeleteAccountView
from django.urls import path

urlpatterns = [
    path('posts/', UserPostView.as_view(), name='user_posts'),
    path('info/', OwnUserDetailView.as_view(), name='user_info'),
    path('info/<int:user_id>/', PublicUserDetailView.as_view(), name='public-user-detail'),
    path('delete/', DeleteAccountView.as_view(), name='delete_account'),
]