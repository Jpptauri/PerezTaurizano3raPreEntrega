from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class FormularioCreacionUsuarios(UserCreationForm):
    username = forms.CharField(label = 'Usuario')
    email = forms.EmailField(label = 'Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label = 'Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir Contraseña',widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        help_texts = {key: '' for key in fields}
        
class FormularioEdicionPerfil(UserChangeForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
    