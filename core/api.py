from rest_framework import generics
from.serializers import *
from django.contrib.auth.models import User
from .models import *

# I wrote this code 

# Create an API endpoint to list all users.
class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# Create an API endpoint to retrieve details of a specific user.
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create an API endpoint to list all profiles.
class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Create an API endpoint to retrieve details of a profile based on user ID.   
class ProfileByUserDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "user_id"

# Create an API endpoint to list all posts by a specific user.
class PostsByUserList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # Customize the queryset based on the user_id provided in the URL.
    def filter_queryset(self, queryset):
        user_id = self.kwargs["user_id"]
        queryset = queryset.filter(user_id = user_id)
        return queryset
# end of code I wrote
