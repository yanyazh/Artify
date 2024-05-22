from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from post.serializers import PostSerializer


# Create your views here.

class UserPostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        posts = Post.objects.filter(user_id=request.user.id)
        serializer = PostSerializer(posts, many=True)

        return Response({'posts': serializer.data})
