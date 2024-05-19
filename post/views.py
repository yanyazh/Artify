from rest_framework.viewsets import ModelViewSet
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def create(self, request):
    #     print(request.headers)
    #     return Response("hello")
    
    def get_queryset(self):
        queryset = Post.objects.all().select_related('user_id') 
        
        post_id = self.request.query_params.get('id')
        if post_id:
            queryset = queryset.filter(id=post_id)
        return queryset

class LikeViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    def get_queryset(self):
        queryset = Like.objects.all()
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset
    