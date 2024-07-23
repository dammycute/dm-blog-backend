from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_fields = ['id',]


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['bio', 'socio_insta', 'socio_x', 'website']
        read_only_fields = ['author', 'date_posted',]

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {
            "password": {"write_only": True}
        }
        read_only_fields = ['id',]

    def create(self, validated_data):
        profile_data = validated_data.pop( 'profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        return user
    

