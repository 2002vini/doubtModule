from django.shortcuts import render
from . models import *
import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet


def getRoomHash(sender_id, receiver_id):
    room_name = ""
    if str(sender_id) > str(receiver_id):
        room_name = f"{sender_id}--{receiver_id}"
    else:
        room_name = f"{receiver_id}--{sender_id}"

    room_id = hashlib.sha256(room_name.encode()).hexdigest()
    return room_id

class DoubtApi(ViewSet):
    #it returns the doubtroom and messages object of doubtroom
    @action(methods=['get'], detail=False, url_path='room_id')
    def getRoomId(self,request):
        student_profile=Profile.objects.get(user=request.user)
        teacher_profile=Profile.objects.get(user=student_profile.teacher)
        room_id = getRoomHash(student_profile.unique_id,teacher_profile.unique_id)

        if not ChatRoom.objects.filter(room_id=room_id).exists():
            ChatRoom.objects.create(room_id=room_id)

        chatroom = ChatRoom.objects.get(room_id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)

        chatroom_serializer=ChatRoomSerializer(chatroom)
        messages_serializer=ChatMessageSerializer(messages,many=True)
        return Response({"roomid":chatroom.room_id,"status":200})

    @action(methods=['get'], detail=False, url_path='room')
    def getRoom(self,request):

        student_profile=Profile.objects.get(user=request.user)
        teacher_profile=Profile.objects.get(user=student_profile.teacher)
        room_id = getRoomHash(student_profile.unique_id,teacher_profile.unique_id)

        if not ChatRoom.objects.filter(room_id=room_id).exists():
            ChatRoom.objects.create(room_id=room_id)

        chatroom = ChatRoom.objects.get(room_id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)

        chatroom_serializer=ChatRoomSerializer(chatroom)
        return Response(chatroom_serializer.data,status=200)

    @action(methods=['get'], detail=False, url_path='messages')
    def getChatMessages(self,request):
        student_profile=Profile.objects.get(user=request.user)
        teacher_profile=Profile.objects.get(user=student_profile.teacher)
        room_id = getRoomHash(student_profile.unique_id,teacher_profile.unique_id)
        chatroom = ChatRoom.objects.get(room_id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)

        chatroom_serializer=ChatRoomSerializer(chatroom)
        messages_serializer=ChatMessageSerializer(messages,many=True)
        return Response(messages_serializer.data,status=200)


        

def index(request):
    student_profile=Profile.objects.get(user=request.user)
    teacher_profile=Profile.objects.get(user=student_profile.teacher)
    room_id = getRoomHash(student_profile.unique_id,teacher_profile.unique_id)

    if not ChatRoom.objects.filter(room_id=room_id).exists():
        ChatRoom.objects.create(room_id=room_id)

    chatroom = ChatRoom.objects.get(room_id=room_id)
    messages = ChatMessage.objects.filter(room=chatroom)

    params={
        'room_id':room_id
    }
    return render(request,'chat/home.html',params)

def room(request):
    return render(request,'chat/chatroom.html')


def directMessage(request,room_id):
    sender = Profile.objects.get(user=request.user)
    receiver=Profile.objects.get(user=sender.teacher)
    room_id = getRoomHash(sender.unique_id,receiver.unique_id)
    
    if not ChatRoom.objects.filter(room_id=room_id).exists():
        ChatRoom.objects.create(room_id=room_id)

    chatroom = ChatRoom.objects.get(room_id=room_id)
    messages = ChatMessage.objects.filter(room=chatroom)

    params = {
        
        'room_id': chatroom.room_id,
        'messages': messages,
        'is_direct_message': True,
        'receiver': receiver,
        'receiver_id':receiver.unique_id,
        
    }

    return render(request, 'chat/discussion.html',params)
    


