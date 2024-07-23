from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # fullname = models.CharField(max_length = 256, null=True, b
    bio = models.TextField(max_length=500, blank=True)
    socio_insta = models.CharField(max_length=256, null=True, blank=True)  
    socio_x = models.CharField(max_length=265, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    website = models.CharField(max_length=256, null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"
