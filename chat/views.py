from django.shortcuts import render, redirect
from .models import PublicChatMessage
from django.contrib.auth.decorators import login_required

@login_required 
def public_chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        PublicChatMessage.objects.create(sender=request.user, message=message)
        return redirect('chat:public_chat')
    messages = PublicChatMessage.objects.order_by('-timestamp')[:10]
    return render(request, 'chat/public_chat.html', {'messages': messages})