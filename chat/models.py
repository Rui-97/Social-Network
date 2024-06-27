from django.db import models
from django.contrib.auth.models import User

#  I wrote this code 

# Chatroom model represents a chatroom in the application.
class Chatroom(models.Model):
    # A Many-to-Many relationship with the User model to store chat participants.
    participants = models.ManyToManyField(User, related_name='chatrooms')
    
    def get_latest_messages(self, num_messages=5):
        # Retrieve the latest 'num_messages' messages for the chatroom
        return self.messages.order_by('-timestamp')[:num_messages][::-1]

    
# Message model represents individual messages within a chatroom.   
class Message(models.Model):
    # ForeignKey relationship with Chatroom to associate messages with a specific chatroom.
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="messages")
    # ForeignKey relationship with User to identify the sender of the message.
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    # Text content of the message.
    content = models.TextField()
    # Timestamp records when the message was created (auto-generated).
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender}({self.timestamp:%Y-%m-%d %H:%M}): {self.content}"
# end of code I wrote