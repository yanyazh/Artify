from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from user.models import User
# Create your views here.

class UserCommentsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        
        comments = Comment.objects.filter(user_id=user.id)
        comments_data = list(comments.values('id', 'post_id', 'contents', 'publish_date'))

        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'phone': user.phone,
            'profile_image': user.profile_image.url if user.profile_image else None,
            'is_active': user.is_active,
            'is_admin': user.is_admin,
            'created_at': user.created_at,
            'updated_at': user.updated_at
        }
        return JsonResponse({'user': user_data, 'comments': comments_data}, safe=False)

class PostCommentsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        
        comments = Comment.objects.filter(post_id=post.id)
        comments_data = list(comments.values('id', 'user_id', 'contents', 'publish_date'))
        
        post_data = {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'publish_date': post.publish_date,
            'user_id': post.user_id.id,
            'category_id': post.category_id.id if post.category_id else None,
            # 'post_images': [image.url for image in post.post_images.all()],
            # 'post_tags': [tag.name for tag in post.post_tags.all()]
        }
        
        return JsonResponse({'post': post_data, 'comments': comments_data}, safe=False)

class PostView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        posts = Post.objects.all()

        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            post = serializer.create(serializer.validated_data)
            post.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(APIView):
    def delete(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except:
            return Response({"Message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.user != post.user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class FindPostView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        if request.user != Post.objects.get(id=pk).user_id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(id=pk)

        except:
            return Response({"Message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(PostSerializer(post).data)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        data = request.data.copy()
        data['author'] = request.user.id
        data['post'] = post.id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id, author=request.user)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found or not authorized"}, status=status.HTTP_404_NOT_FOUND)
        
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
