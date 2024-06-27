from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Chatroom, Message

# I wrote this code 
class ChatroomModelTestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')

    def test_chatroom_creation(self):
        # Create a new chatroom
        chatroom = Chatroom.objects.create()
        chatroom.participants.add(self.user1, self.user2)

        # Check if the chatroom was created successfully
        self.assertEqual(Chatroom.objects.count(), 1)
        self.assertEqual(chatroom.participants.count(), 2)
        self.assertTrue(self.user1 in chatroom.participants.all())
        self.assertTrue(self.user2 in chatroom.participants.all())

    def test_get_latest_messages(self):
        # Create a chatroom with messages
        chatroom = Chatroom.objects.create()
        chatroom.participants.add(self.user1, self.user2)

        Message.objects.create(chatroom=chatroom, sender=self.user1, content='Message 1')
        Message.objects.create(chatroom=chatroom, sender=self.user2, content='Message 2')

        # Get the latest messages
        latest_messages = chatroom.get_latest_messages()

        # Check if the latest messages are retrieved correctly
        self.assertEqual(len(latest_messages), 2)
        self.assertEqual(latest_messages[0].content, 'Message 1')
        self.assertEqual(latest_messages[1].content, 'Message 2')

class MessageModelTestCase(TestCase):
    def setUp(self):
        # Create test users and a chatroom
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.chatroom = Chatroom.objects.create()
        self.chatroom.participants.add(self.user1, self.user2)

    def test_message_creation(self):
        # Create a new message
        message = Message.objects.create(chatroom=self.chatroom, sender=self.user1, content='Test Message')

        # Check if the message was created successfully
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(message.chatroom, self.chatroom)
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.content, 'Test Message')

    def test_message_str_method(self):
        # Create a new message
        message = Message.objects.create(chatroom=self.chatroom, sender=self.user1, content='Test Message')

        # Check the __str__ method
        expected_str = f"{self.user1}({message.timestamp:%Y-%m-%d %H:%M}): {message.content}"
        self.assertEqual(str(message), expected_str)
# end of code I wrote
 