from django.test import TestCase
from django.contrib.auth.models import User
import os
from django.conf import settings

from ..models import *

# I wrote this code 

# Test Post Model
class PostModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_post_creation(self):
        # Create a new post
        post = Post.objects.create(
            user=self.user,
            caption='Test Caption',
        )

        # Check if the post was created successfully
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.caption, 'Test Caption')

    def test_post_str_method(self):
        # Create a new post
        post = Post.objects.create(
            user=self.user,
            caption='Test Caption',
        )

        # Check the __str__ method
        expected_str = f"{self.user}({post.created_time:%Y-%m-%d %H:%M}): {post.caption}"
        self.assertEqual(str(post), expected_str)

    def test_post_image_upload(self):
        # Create a new post with an image
        post = Post.objects.create(
            user=self.user,
            caption='Test Caption',
            image= os.path.join(settings.MEDIA_ROOT, "test.jpg"),
        )

        # Check if the image field is not empty
        self.assertIsNotNone(post.image)

    def test_post_created_time_auto_add(self):
        # Create a new post
        post = Post.objects.create(
            user=self.user,
            caption='Test Caption',
        )

        # Check if the created_time field was automatically set
        self.assertIsNotNone(post.created_time)

    def test_post_related_name(self):
        # Create a new user and post
        user = User.objects.create(username='anotheruser', password='anotherpassword')
        post = Post.objects.create(
            user=user,
            caption='Another Test Caption',
        )

        # Check if the related name works correctly
        self.assertEqual(user.posts.count(), 1)
        self.assertEqual(user.posts.first(), post)



# Test Profile Model
class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser', password='testpassword')

    def test_profile_creation(self):
        # Update automatically created profile
        profile = Profile.objects.get(user=self.user)
        profile.bio = 'Test Bio'
        profile.location = 'Test Location'
       

        # Check if the profile was created successfully
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(profile.bio, 'Test Bio')
        self.assertEqual(profile.location, 'Test Location')

    def test_profile_str_method(self):
        # Update automatically created profile
        profile = Profile.objects.get(user=self.user)
        profile.bio = 'Test Bio'
        profile.location = 'Test Location'

        # Check the __str__ method
        self.assertEqual(str(profile), self.user.username)

    def test_number_of_following(self):
        # add a new follows in the automatically created profile
        profile = Profile.objects.get(user=self.user)
        another_user = User.objects.create(username='anotheruser', password='anotherpassword')
        profile.follows.add(another_user.profile)

        # Check the number of following
        self.assertEqual(profile.number_of_following(), 1)

    def test_number_of_followers(self):
        profile = Profile.objects.get(user=self.user)
        another_user = User.objects.create(username='anotheruser', password='anotherpassword')
        another_user.profile.follows.add(profile)

        # Check the number of followers
        self.assertEqual(profile.number_of_followers(), 1)

# end of code I wrote

