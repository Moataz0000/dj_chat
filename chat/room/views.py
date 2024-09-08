from django.shortcuts import render, get_object_or_404
from .models import Room, Message
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms':rooms})



@login_required(login_url='login')
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug, is_active=True)
    messages = Message.objects.filter(room=room, is_active=True)[:25]
    return render(request, 'room/room_detail.html', {'room':room, 'messages':messages})
