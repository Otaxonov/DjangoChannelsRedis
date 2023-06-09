from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatRoomsView, name='chat_rooms'),
    path('chat/<str:room_name>/', views.ChatRoomView, name='chat_room')
]