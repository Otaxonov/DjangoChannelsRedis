from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Room, Message

# Create your views here.

def HomeView(request):

    context = {
        'title': 'DjangoChat',
    }

    return render(request, 'Chat/home.html', context)

@login_required
def RoomsView(request):

    rooms = Room.objects.all()

    context = {
        'title': 'Chat Rooms',
        'rooms': rooms
    }

    return render(request, 'Chat/rooms.html', context)

@login_required
def RoomView(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)

    context = {
        'title': 'Chat Room',
        'room': room,
        'room_messages': messages,
    }

    return render(request, 'Chat/room.html', context)
