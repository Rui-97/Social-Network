from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# I wrote this code 
class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ["id","username", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
# end of code I wrote
