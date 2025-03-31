from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Blog(models.Model):
    CATEGORY = [
        ('Lifestyle', 'Lifestyle'),
        ('Technology', 'Technology'),
        ('Culture', 'Culture'),
        ('Sports', 'Sports'),
        ('Business', 'Business'),
        ('Travel', 'Travel'),
        ('Economy', 'Economy'),
    ]
    title = models.CharField(max_length=200)
    post = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY)
    # tag = models.CharField(max_length=20, null=True, blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    

class ImageUploadModel(models.Model):
    image = CloudinaryField('images', blank=True, null=True)
    
class Comment(models.Model):
    post = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " commented on " + self.post.title
    
    
