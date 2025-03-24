from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'post', 'date_posted', 'author_username', 'category', 'image', 'image_url']
        read_only_fields = ['id', 'author', 'date', 'image_url']
        

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadModel
        fields = ['image']
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment', 'name', 'date_posted']
        