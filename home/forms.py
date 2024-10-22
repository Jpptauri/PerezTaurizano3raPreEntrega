from django import forms

class CrearMascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    especie = forms.CharField(max_length=20)
    edad = forms.IntegerField()