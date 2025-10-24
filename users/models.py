from django.db import models
from django.contrib.auth.models import User

class Tareas(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300, blank=True)
    estado = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=999999)