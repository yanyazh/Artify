from user.views import UserPostView, OwnUserDetailView, PublicUserDetailView, DeleteAccountView, EditUserProfileView
from django.urls import path

urlpatterns = [
    path('posts/', UserPostView.as_view(), name='user_posts'),
    path('info/', OwnUserDetailView.as_view(), name='user_info'),
    path('info/<int:user_id>/', PublicUserDetailView.as_view(), name='public-user-detail'),
    path('delete/', DeleteAccountView.as_view(), name='delete_account'),
    path('edit/', EditUserProfileView.as_view(), name='edit_user_profile'),  # New endpoint for editing user profile
]
