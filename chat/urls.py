from django.urls import path
from . import views

#  I wrote this code 
urlpatterns = [
    path("list",views.chat_list,name="chat_list" ),
    path("chatroom/<str:chatroom_name>", views.chat_room, name="chatroom"),
]
# end of code I wrote