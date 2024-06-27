from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import *
from ..forms import *

# I wrote this code 
class ViewTestCase(TestCase):
    def setUp(self):
        # Create a test user and log them in for testing views that require authentication
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.get(user=self.user)
        self.client.login(username='testuser', password='testpassword')

    def test_landing_view(self):
        # Test the landing view
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)  # Check if the response status is 200 (OK)

    def test_register_view(self):
        # Test the register view
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)  # Check if the response status is 200 (OK)

        # Test user registration form submission
        response = self.client.post(reverse('register'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertRedirects(response, reverse('login'))  # Check if the redirect URL is correct

    def test_login_view(self):
        # Test the login view
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)  # Check if the response status is 200 (OK)

        # Test user login form submission
        response = self.client.post(reverse('login'), data={
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertRedirects(response, reverse('home', args=[self.user.id]))  # Check if the redirect URL is correct


    def test_delete_post_view(self):
        # Test the delete post view
        post = Post.objects.create(user=self.user, caption='Test Post')
        response = self.client.post(reverse('delete_post', args=[post.id]))
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect
        self.assertRedirects(response, reverse('home', args=[self.user.id]))  # Check if the redirect URL is correct

    def test_api_index_view(self):
        # Test the API index view
        response = self.client.get(reverse('api_index'))
        self.assertEqual(response.status_code, 200)  # Check if the response status is 200 (OK)
# end of code I wrote
