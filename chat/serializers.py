from .models import *
from rest_framework.serializers import ModelSerializer

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model=ChatRoom
        fields = "__all__"


class ChatMessageSerializer(ModelSerializer):
    class Meta:
        model=ChatMessage
        fields = "__all__"