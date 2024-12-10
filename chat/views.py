from django.shortcuts import render,HttpResponse,redirect
from chat.models import room as rooom,message

# Create your views here.

def index(request):
    return render(request,'form.html')

def room(request,room):    
    username = request.GET.get('username')
    rom_d=rooom.objects.get(name=room)
    messages=message.objects.filter(room=room)
    return render(request,'room.html',{'room':rom_d,'username':username,'message':messages})
    
def room_validate(request):    
    if request.method == 'POST':
        room_name = request.POST.get('room-name')
        username = request.POST.get('username')
        if rooom.objects.filter(name=room_name).exists():
            return redirect(f'/{room_name}/?username={username}')
        else:
            new_room = rooom.objects.create(name=room_name)
            new_room.save()
            return redirect(f'/{room_name}/?username={username}')

def send(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        messages = request.POST.get('message')
        room = request.POST.get('room')
        new_message = message.objects.create(user=user,value=messages,room=room)
        new_message.save()
        return HttpResponse('Message sent successfully')


