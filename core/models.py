from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# I wrote this code 
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posts")
    image = models.ImageField(upload_to= "post_imgs", blank=True, null = True)
    caption = models.CharField(max_length=200)
    # Automatically set the field to now when the object is first create
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}({self.created_time:%Y-%m-%d %H:%M}): {self.caption}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    follows = models.ManyToManyField("self", symmetrical=False, related_name="followed_by", blank=True) # self-referential many-to-many relationship
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to= "profile_imgs", default="profile_imgs/default_profile_img.jpg", blank=True)
    
    def __str__(self):
	    return self.user.username
    
    def number_of_following(self):
        # Subtracte the user themself
        return self.follows.count()-1
    
    def number_of_followers(self):
        # Subtracte the user themself
        return self.followed_by.count()-1

# Create a new profile when a new user is registered
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        # Have the new user follows themself
        profile.follows.set([profile.id])
        profile.save()

# The reciver function create_profile will get called when the post_save signal is sent
post_save.connect(create_profile, sender = User)
# end of code I wrote
