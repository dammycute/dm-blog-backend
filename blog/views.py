from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Random
import cloudinary

# Create your views here.
# This view is for the authors. This allows them to create and view what they've created. 
class BlogCreationView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields  = ["id", "title", "post", "author", 'category']
    search_fields  = ["id", "title", "post", "author", 'category']
    ordering_fields  = ["id", "title", "post", "author", 'category']
    
    # print(Blog.author)

    def perform_create(self, serializer):
        blog = serializer.save(author = self.request.user)
        
        if blog.image:
            try:
                upload_result = cloudinary.uploader.upload('<file_path>')
                image_url = upload_result.get('secure_url')
                serializer.save(image_url=image_url)
            except Exception as e:
                print(f"Error uploading image: {e}")
        return blog
    
    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user)


class BlogUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user)
    


class BlogPostListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields  = ["id", "title", "post", "author", 'category']
    search_fields  = ["id", "title", "post", 'category']
    ordering_fields  = ["id", "title", "post", "author", 'category']
    
    def get_queryset(self):
        return Blog.objects.all().order_by(Random())
    
    
class BlogPostRetrievalView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    

class ImageUploadView(generics.ListCreateAPIView):
    queryset = ImageUploadModel.objects.all()
    serializer_class = ImageUploadSerializer
    

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticated,)
    
