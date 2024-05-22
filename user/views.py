from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer
from .serializers import UserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny

from .models import User
# Create your views here.

class UserPostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.filter(user_id=request.user.id)
        serializer = PostSerializer(posts, many=True)

        return Response({'posts': serializer.data})

class OwnUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class PublicUserDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")

        serializer = UserSerializer(user)
        return Response(serializer.data)