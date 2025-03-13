from django import forms
from django.contrib.auth.models import User
from users.models import Tareas
from django.core.exceptions import ValidationError

class Inicio_Sesion(forms.Form):
    """formulario de inicio de sesion con respecto a el modielo usuario que viene con django"""
    username = forms.CharField(widget=forms.TextInput,label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")


class New_Cuenta(forms.ModelForm):
    """formulario de registrarse con respecto a el modelo usuario que viene con django 
    hereda de Inicio Sesion para reutilizar el codigo creado por este"""
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta():
        model = User
        fields =  ["username", "password","confirm_password"] 
         

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden")

        return cleaned_data
    
    def save(self,commit=True):
        user= super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if user:
            user.save()
            return user
        return None

class New_Tarea(forms.Form):
    """formulario para agregar una nueva tarea"""
    nombre = forms.CharField(widget= forms.TextInput,label= "Nombre de la tarea")
    descripcion = forms.CharField(widget=forms.Textarea,label="Descripción",max_length=9999)


        