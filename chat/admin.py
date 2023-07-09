from django.contrib import admin
from .models import *
# Register your models here.
#profile model
#doubt model
class CustomChatRoom(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'room_id']

class CustomChatMessage(admin.ModelAdmin):
    list_display = ['id', 'sender', 'room', 'created_at', 'message_content']

class CustomProfile(admin.ModelAdmin):
    list_display=['user','unique_id','teacher']
    
admin.site.register(Profile,CustomProfile)
admin.site.register(ChatRoom,CustomChatRoom)
admin.site.register(ChatMessage,CustomChatMessage)