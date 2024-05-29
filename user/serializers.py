from rest_framework import serializers
from .models import User, Image

class UserSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'name', 'first_name', 'last_name', 'bio', 'email', 
            'phone', 'profile_image', 'profile_image_url', 
            'follower_count', 'following_count'
        ]
        read_only_fields = ['email', 'follower_count', 'following_count', 'profile_image_url']

    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.file.url
        return None

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone = validated_data.get('phone', instance.phone)
        if 'profile_image' in validated_data:
            instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance
