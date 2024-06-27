import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from .models import Chatroom, Message

#  I wrote this code 
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.room_group_name = f'chat_{self.chatroom_id}'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # remove the channel from the group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chatroom_id = text_data_json['chatroomId']
        message = text_data_json['message']
        user = self.scope["user"]

        # Save message to the database
        chatroom = Chatroom.objects.get(id=chatroom_id)
        message_obj = Message(chatroom=chatroom, content=message, sender=user)
        message_obj.save()
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                # the chat_message function will be invoked on consumers that receive the event.
                'type':'chat.message',
                'message':message,
                'sender': user.username,
                'timestamp': str(message_obj.timestamp)
            }
        )
    # Receive the event from room group 
    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp =event['timestamp']
        
        self.send(
            text_data=json.dumps({
            'message':message,
            'sender': sender,
            'timestamp': timestamp
        }))
# end of code I wrote
