from django.shortcuts import render, redirect
from .models import ChatPublico
from django.contrib.auth.decorators import login_required

@login_required 
def chat_publico(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        ChatPublico.objects.create(usuario=request.user, mensaje=mensaje)
        return redirect('chat:chat_publico')
    mensajes = ChatPublico.objects.order_by('-horario_envio')[:10]
    return render(request, 'chat/chat_publico.html', {'mensajes': mensajes})