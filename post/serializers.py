from rest_framework.serializers import ModelSerializer
from .models import Post, Comment, Like
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'likes_count',  'publish_date', 'user_id', 'category_id', 'post_images')
        
    def get_likes_count(self, obj):
        return Like.objects.filter(post_id=obj.id).count()

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('contents', 'publish_date', 'post_id', 'user_id')
        read_only_fields = ['user_id', 'post_id', 'publish_date']
