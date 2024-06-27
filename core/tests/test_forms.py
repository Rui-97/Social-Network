from django.test import TestCase
from django.contrib.auth.models import User
import os
from django.conf import settings

from ..forms import *
from ..models import *

# I wrote this code 
class RegisterFormTestCase(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = RegisterForm(data=form_data)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'mismatchedpassword',
        }
        form = RegisterForm(data=form_data)

        # Check if the form is not valid due to password mismatch
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_unique_username(self):
        # Create a user with the same username to test uniqueness
        User.objects.create_user(username='testuser', password='testpassword123')

        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = RegisterForm(data=form_data)

        # Check if the form is not valid due to a non-unique username
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_weak_password(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'weak',
            'password2': 'weak',
        }
        form = RegisterForm(data=form_data)

        # Check if the form is not valid due to a weak password
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)



class ProfileFormTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='testuser', password='testpassword')
        # Get the profile automaticalliy created for the user
        self.profile = Profile.objects.get(user = self.user)

    def test_valid_profile_form(self):
        form_data = {
            'bio': 'Test Bio',
            'location': 'Test Location',
            'image': None,  
        }
        form = ProfileForm(data=form_data, instance=self.profile)

        # Check if the form is valid
        self.assertTrue(form.is_valid())

    def test_empty_location(self):
        form_data = {
            'bio': 'Test Bio',
            'location': '',  # Empty location
            'image': None, 

        }
        form = ProfileForm(data=form_data, instance=self.profile)

        # Check if the form is valid (location field is optional)
        self.assertTrue(form.is_valid())

    def test_valid_image(self):
        form_data = {
            'bio': 'Test Bio',
            'location': 'Test Location',
            'image': os.path.join(settings.MEDIA_ROOT, "test.jpg"), 
        }
        form = ProfileForm(data=form_data, instance=self.profile)

        # Check if the form is valid
        self.assertTrue(form.is_valid())
# end of code I wrote
