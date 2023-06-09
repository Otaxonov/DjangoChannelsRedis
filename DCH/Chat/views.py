from django.shortcuts import render

# Create your views here.

def ChatRoomsView(request):

    context = {
        "title": "Chat Rooms"
    }

    return render(request, 'chat/rooms.html', context)

def ChatRoomView(request, room_name):

    context = {
        "title": "Chat Room",
        "room_name": room_name
    }

    return render(request, 'chat/room.html', context)