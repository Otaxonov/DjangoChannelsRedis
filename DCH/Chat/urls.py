from django.urls import path
from .views import HomeView, RoomsView, RoomView

urlpatterns = [
    path('', HomeView, name='chat_home'),
    path('rooms/', RoomsView, name='chat_rooms'),
    path('room/<slug:slug>', RoomView, name='chat_room'),
]