
from django.contrib import admin
from django.urls import path,include
from . import views
from . views import DoubtApi

urlpatterns = [
    path('', views.index , name='index'),
    path('room/<str:room_id>/',views.directMessage,name='directMessage'),
    path('doubt/room_id/', DoubtApi.as_view({'get': 'getRoomId'}), name='doubt-room-id'),
    path('doubt/room/', DoubtApi.as_view({'get': 'getRoom'}), name='doubt-room'),
    path('doubt/messages/', DoubtApi.as_view({'get': 'getChatMessages'}), name='doubt-messages'),

    #path('<str:room_name>/',views.room,name='room'),
   
]
