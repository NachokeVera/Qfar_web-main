from django.contrib.auth.models import User
from django.db import models

#Modelos correspondientes a los tipos de usuarios
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paciente')
    cesfam = models.CharField(max_length=40)
    sintomas = models.TextField()
    peso = models.IntegerField()
    esperando = models.BooleanField(default=False)

class QuimicoFarmaceutico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='quimico_farmaceutico')
    universidad = models.CharField(max_length=60)
    titulo = models.CharField(max_length=60)
    curriculum = models.TextField()
    horario_disponible = models.CharField(max_length=60)
    #foto_perfil = models.CharField(max_length=200, unique=True)
    numero_registro = models.CharField(max_length=60)

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    fecha_de_nacimiento = models.DateField()
    
class AreaMedica(models.Model):
    area_medica = models.CharField(max_length=25)

#Tablas de chat

class Chat(models.Model):
    dialogId = models.TextField()

class UsusariosChat(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_quimico = models.ForeignKey(QuimicoFarmaceutico, on_delete=models.CASCADE)
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)