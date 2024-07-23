from django.shortcuts import render
from rest_framework import generics
from .serializers import  * 
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class ProfileEditView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'id'

    def perform_update(self, serializer):
        return serializer.save(User=self.request.user)

