from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
post_router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(post_router.urls)),   
]