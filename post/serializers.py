from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'publish_date', 'user_id', 'category_id', 'post_images')

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('contents', 'publish_date', 'post_id', 'user_id')
        read_only_fields = ['user_id', 'post_id', 'publish_date']
