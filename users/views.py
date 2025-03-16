from django.shortcuts import render, redirect,get_object_or_404
from users.formulario import Inicio_Sesion,New_Cuenta,New_Tarea
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from users.models import Tareas



def inicio(request):
    """esta vista se encarga de mostrar el inicio del sitio permitiondo al usuario 
    iniciar sesion en el sitio, tambien compruba que las credenciales sean validas en la DATABASE""" 
    if request.POST:
        formulario = Inicio_Sesion(request.POST)
        if formulario.is_valid():
            usuario = authenticate(request,username=formulario.cleaned_data["username"],
                                   password=formulario.cleaned_data["password"])
            if usuario:
                login(request,usuario)
                return tarea(request)
            else:
                formulario.add_error(None,"cerifica tu identidad, el usuario y la contraseña\
                                      no coinciden con nuestra base datos")
 
    else:formulario = Inicio_Sesion()     

    return render(request,"inicio.html",{'formulario_django':formulario})

def registrarse(request):
    """Esta vista se encarga de verificar la validez del registro para almacenar un nuevo usuario en la 
    DATABASE , verifica que no se creen usuarios con otro  username de usuario ya guardado"""
    if request.POST:
        formulario = New_Cuenta(request.POST)
        if formulario.is_valid():
            if formulario.save():
                return redirect('inicio')
            else:formulario.add_error(None,"No se puso registrar el usuario cambie su nombre")
    else:
        formulario= New_Cuenta()

    return render(request,"registro.html",{'formulario_django':formulario})

@login_required
def tarea(request):

    usuario = request.user
    tareas = Tareas.objects.filter(users= usuario)
    if request.POST:
        id_tarea = request.POST.get("tarea_id")
        if id_tarea:
            task = get_object_or_404(Tareas, users=usuario, id=id_tarea)
            task.estado= not task.estado
            task.save()
            redirect('tarea')
    return render(request,"tareas.html",{'tarea_all':tareas})

@login_required
def nueva_tarea(request):
    if request.POST:
        usuario = request.user
        form = New_Tarea(request.POST)
        if form.is_valid():
            try:
                form.save(usuario=usuario)  # Guardar la tarea para el usuario actual
                return redirect("tarea")  # Redirigir para evitar reenvío del formulario
            except ValidationError as e:
                form.add_error("nombre", e.message)
    else:
        form = New_Tarea()
    return render(request,"nueva_tarea.html",{'formulario_tarea':form})
 
@login_required
def delete_tarea(request):
    if request.POST:
        id_tarea = request.POST.get("tarea_id")
        if id_tarea:
            Tareas.objects.filter(id = id_tarea).delete()
    return redirect('tarea')