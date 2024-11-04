from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('chat-publico/', views.chat_publico, name='chat_publico'),
]