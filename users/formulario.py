from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Inicio_Sesion(forms.ModelForm):
    """formulario de inicio de sesion con respecto a el modielo usuario que viene con django"""
    username = forms.CharField(widget=forms.TextInput,label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class New_Cuenta(forms.ModelForm):
    """formulario de registrarse con respecto a el modelo usuario que viene con django 
    hereda de Inicio Sesion para reutilizar el codigo creado por este"""
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta():
        fields =  ["username", "password","confirm_password"]  

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    
    def


