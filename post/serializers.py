from rest_framework.serializers import ModelSerializer
from .models import Post, Comment, Like
from rest_framework import serializers
from misc.serializers import ImageSerializer 

class PostSerializer(ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    post_images = ImageSerializer(many=True)
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

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'like_date', 'post_id', 'user_id')
        # read_only_fields = ('like_date')

class CreateLikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('post_id')