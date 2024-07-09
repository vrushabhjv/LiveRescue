import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatMessage, Room
from django.contrib.auth.models import User
from html import escape

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name'] # get the room name from the url route
        self.room_group_name = 'chat_%s' % self.room_name # create a group name for the room
        print(f"From ChatConsumer: Connecting to room: {self.room_name}")

        # join the room group
        
        await self.channel_layer.group_add( # add the user to the group
            self.room_group_name, # group name
            self.channel_name # channel name 
        )
        print("Accepting connect requests")
        await self.accept() # accept the connection

    async def disconnect(self, close_code): # disconnect the user
        print("Disconnecting from room")
        # leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"Disconnected from room : {self.room_group_name}")
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        
        await self.save_message(username, room, message) # Save the message to the database
        
        # The receive() function is the main entry point for handling incoming WebSocket messages in the 'ChatConsumer' class. It is responsible for processing the client's message, storing it in the database, and then broadcasting it to all other clients in the same room.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':message,
                'username':username,
                'room':room,
            }
        )
        
    # this function is called when a message is received from the group 
    # it sends the message to the client
    async def chat_message(self, event):
        message = escape(event['message'])
        username = escape(event['username'])
        room = event['room']
        
        await self.send(text_data=json.dumps({
            'message':message,
            'username':username,
            'room':room,
        }))
        
    @sync_to_async
    def save_message(self, username, room, chatmessage):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        
        ChatMessage.objects.create(user=user, room=room, content=chatmessage)