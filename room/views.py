from django.shortcuts import render, redirect
from .models import Room, ChatMessage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
# the @login_required decorator will ensure that only authenticated users can access the view below this particular decorator. 
# If a user is not authenticated, they will be redirected to the login page. 
# This is useful for ensuring that only authenticated users can access certain pages.
def rooms(request):
    rooms= Room.objects.all()
    
    return render(request,'room/rooms.html', {"rooms":rooms})

@login_required(login_url='login')
def room(request, slug):
    room = Room.objects.get(slug=slug)
    # chatmessages = ChatMessage.objects.filter(room=room)[0:25]
    chatmessages = ChatMessage.objects.filter(room=room).order_by('-date_added')[0:25][::-1]
    print(chatmessages)
    
    return render(request, 'room/room.html', {'room':room, 'chatmessages':chatmessages})

@login_required(login_url='login')
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        room_name_slug = room_name.replace(" ", "-").lower()
        print(room_name, room_name_slug)
        if room_name:
            room = Room.objects.create(name=room_name, slug=room_name_slug)
            return redirect('rooms')
        print("inside create room")
    else:
        return render(request, 'room/createRoom.html')    
    