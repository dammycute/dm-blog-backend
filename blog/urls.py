from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogCreationView.as_view(), name='create-blog'),
    path('list', BlogPostListView.as_view(), name='blog-list'),
    path('<int:id>', BlogUpdateView.as_view(), name='blog-update'),
    path('list/<int:id>', BlogPostRetrievalView.as_view(), name = 'blogdetails'),
    path('image-upload', ImageUploadView.as_view(), name= 'image-upload'),
    path('comments', CommentView.as_view(), name='comment'),
]