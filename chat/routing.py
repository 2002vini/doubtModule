from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/socket-server/<str:room_id>',consumers.chatConsumer.as_asgi()),
]