import json
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from . models import *

class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name=self.scope['url_route']['kwargs']['room_id']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self,text_data):
        print("we have received a message")
        print(text_data)
        data = json.loads(text_data)
        message_sender = data['message_sender']
        message_content = data['message']
        

        await self.channel_layer.group_send(        # this line sends message to all the channels in the group
            self.group_name,
            {
                'type': 'chat_message',      # this method will be used to send message individually to all users
                'message_content': message_content,
                'message_sender': message_sender
            }
        )
        await self.save_message(message_sender,self.group_name,message_content)

       
    async def chat_message(self,event):
        message_content = event['message_content']
        message_sender = event['message_sender']
        await self.send(text_data=json.dumps(
            {
                'type':'chat_message',
                'message_content': message_content,
                'message_sender': message_sender
            }
        ))
    
    @sync_to_async
    def save_message(self,message_sender,group_name,message_content):
        sender = User.objects.get(username=message_sender)
        sender_profile=Profile.objects.get(user=sender)
        sender_profile.last_text=message_content
        room = ChatRoom.objects.get(room_id=group_name)
        chat_obj = ChatMessage(sender=sender, room=room, message_content=message_content)
        chat_obj.save()
        