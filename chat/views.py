from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from chat.models import room as rooom, message
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'choice.html')

def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room-name')
        username = request.POST.get('username')
        if rooom.objects.filter(name=room_name).exists():
            messages.error(request, 'Room already exists')
        else:
            new_room = rooom.objects.create(name=room_name)
            new_room.save()
            return redirect(f'/{room_name}/?username={username}')
    return render(request, 'create.html')

def join_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room-name')
        username = request.POST.get('username')
        if rooom.objects.filter(name=room_name).exists():
            return redirect(f'/{room_name}/?username={username}')
        else:
            messages.error(request, 'Room does not exist')
    return render(request, 'join.html')

def room(request, room):    
    username = request.GET.get('username')
    rom_d = rooom.objects.get(name=room)
    return render(request, 'room.html', {'room': rom_d, 'username': username})
    
# def room_validate(request):    
#     if request.method == 'POST':
#         room_name = request.POST.get('room-name')
#         username = request.POST.get('username')
#         if rooom.objects.filter(name=room_name).exists():
#             return redirect(f'/{room_name}/?username={username}')
#         else:
#             new_room = rooom.objects.create(name=room_name)
#             new_room.save()
#             return redirect(f'/{room_name}/?username={username}')

def send(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        messages = request.POST.get('message')
        room = request.POST.get('room')
        new_message = message.objects.create(user=user,value=messages,room=room)
        new_message.save()

def getMessages(request, room):
    room_obj = rooom.objects.get(name=room)  # Corrected: rooom instead of room
    messages = message.objects.filter(room=room_obj)
    
    # Return formatted messages as a list of dictionaries
    messages_list = [
        {
            "user": msg.user,
            "value": msg.value,
            "date": msg.date.strftime('%Y-%m-%d %H:%M:%S')  # Format date for display
        }
        for msg in messages
    ]
    
    return JsonResponse(messages_list, safe=False)  # Returning list of messages in JSON format
