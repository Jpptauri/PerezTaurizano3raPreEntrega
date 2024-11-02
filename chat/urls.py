from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('public-chat/', views.public_chat, name='public_chat'),
]