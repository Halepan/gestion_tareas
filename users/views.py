from django.shortcuts import render, redirect
from users.formulario import Inicio_Sesion,New_Cuenta
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



def inicio(request):
    """esta vista se encarga de mostrar el inicio del sitio permitiondo al usuario 
    iniciar sesion en el sitio, tambien compruba que las credenciales sean validas en la DATABASE""" 
    if request.POST:
        formulario = Inicio_Sesion(request.POST)
        if formulario.is_valid():
            usuario = authenticate(request,formulario.cleaned_data["username"],
                                   formulario.cleaned_data["password"])
            if usuario:
                return HttpResponse("valido")
            else: return HttpResponse("o el usuario es incorrecto o la contraseña no es valida")
            

    return render(request,"inicio.html",{'formulario_django':Inicio_Sesion()})

def registrarse(request):
    """Esta vista se encarga de verificar la validez del registro para almacenar un nuevo usuario en la 
    DATABASE , verifica que no se creen usuarios con otro  username de usuario ya guardado"""
    if request.POST:
        formulario = New_Cuenta(request.POST)
        if formulario.is_valid():
                    
            if not User.objects.filter(username= formulario.cleaned_data['username']):
                user = User(username= formulario.cleaned_data['username'],
                         password = formulario.cleaned_data['password'])
                user.save()
                return redirect('inicio')

    return render(request,"registro.html",{'formulario_django':New_Cuenta()})


    
 