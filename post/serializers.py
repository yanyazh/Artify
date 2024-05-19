from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Post, Like
from auth.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    likes_count = SerializerMethodField()
    user_id = UserSerializer()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'publish_date', 'user_id', 'likes_count', 'category_id')
    
    def get_likes_count(self, obj):
        return Like.objects.filter(post_id=obj.id).count()
    
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'like_date', 'post_id', 'user_id')
        # read_only_fields = ('like_date')

class CreateLikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('post_id')