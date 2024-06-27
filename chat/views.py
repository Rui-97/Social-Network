from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core.models import Profile
from .models import Chatroom, Message

# I wrote this code 

# The chat_list view displays a list of chatrooms for the logged-in user.
@login_required(login_url="/login/")
def chat_list(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request,"chat/chat_list.html", {"profile": profile})

# The chat_room view handles individual chatrooms between users.
@login_required(login_url="/login/")
def chat_room(request, chatroom_name):
    # Identify the sender as the currently logged-in user.
    sender = request.user
    # Extract the username of the chat receiver from the chatroom_name.
    for participant in chatroom_name.split("_"):
        if participant != sender.username:
            reciverName = participant
    reciver = User.objects.get(username = reciverName)
    
    # if a chatroom instance for the sender and reciver already exists in the database, query the existing chatroom
    # otherwise, create a new chatroom instance for the sender and recirver
    chatroom_queryset = Chatroom.objects.filter(participants=sender).filter(participants=reciver)
    if chatroom_queryset:
        current_chatroom = chatroom_queryset[0]
    else:
        # create a Chatroom instance in database
        current_chatroom = Chatroom()
        current_chatroom.save()
        current_chatroom.participants.add(sender)
        current_chatroom.participants.add(reciver)
        current_chatroom.save()
    
    # Get history messages of the current chatroom
    history_messages = current_chatroom.get_latest_messages(5)
        
    context = {
        "chatroom_id": current_chatroom.id,
        "reciver": reciver,
        "history_messages": history_messages
    }
    return render(request, "chat/chat_room.html", context)
# end of code I wrote
