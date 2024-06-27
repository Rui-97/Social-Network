from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Profile
from ..models import Chatroom
from ..views import chat_list, chat_room

#  I wrote this code 
class ChatViewsTestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.client = Client()

    def test_chat_list_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Access the chat_list view
        response = self.client.get(reverse('chat_list'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_chat_room_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Create another user for the chat room
        user2 = User.objects.create_user(username='user2', password='user2password')

        # Create a chatroom instance
        chatroom = Chatroom.objects.create()
        chatroom.participants.add(self.user, user2)

        # Access the chat_room view
        chatroom_name = f"{self.user.username}_{user2.username}"
        response = self.client.get(reverse('chatroom', args=[chatroom_name]))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_chat_room_creation(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Create another user for the chat room
        user2 = User.objects.create_user(username='user2', password='user2password')

        # Access the chat_room view with a new chatroom name
        chatroom_name = f"{self.user.username}_{user2.username}"
        response = self.client.get(reverse('chatroom', args=[chatroom_name]))

        # Check if a new chatroom is created
        chatroom = Chatroom.objects.filter(participants=self.user).filter(participants=user2)
        self.assertTrue(chatroom.exists())

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_chat_room_existing(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpassword')

        # Create another user for the chat room
        user2 = User.objects.create_user(username='user2', password='user2password')

        # Create an existing chatroom
        chatroom = Chatroom.objects.create()
        chatroom.participants.add(self.user, user2)

        # Access the chat_room view with the same chatroom name
        chatroom_name = f"{self.user.username}_{user2.username}"
        response = self.client.get(reverse('chatroom', args=[chatroom_name]))

        # Check if the existing chatroom is used
        self.assertEqual(chatroom.id, response.context['chatroom_id'])

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
# end of code I wrote
