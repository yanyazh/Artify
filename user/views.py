from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from post.models import Post
from post.serializers import PostSerializer
from .serializers import UserSerializer
from .models import User

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

class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class EditUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
