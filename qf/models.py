from django.contrib.auth.models import User
from django.db import models

#Modelos correspondientes a los tipos de usuarios
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='paciente')
    cesfam = models.CharField(max_length=40)
    sintomas = models.TextField()
    peso = models.IntegerField()
    esperando = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.username

class Especialidad(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id de la especialidad')
    especialidad= models.CharField(max_length=20, verbose_name='nombre de la especialidad', null=False, blank=False)

    def __str__(self) -> str:
        return self.especialidad
    
class AreaMedica(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id de la area medica')
    area_medica= models.CharField(max_length=20, verbose_name='nombre de la area', null=False, blank=False)

    def __str__(self) -> str:
        return self.area_medica

class QuimicoFarmaceutico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='quimico_farmaceutico')
    universidad = models.CharField(max_length=60)
    titulo = models.CharField(max_length=60)
    curriculum = models.TextField()
    horario_disponible = models.CharField(max_length=60)
    #foto_perfil = models.CharField(max_length=200, unique=True)
    numero_registro = models.CharField(max_length=60)
    especialidades = models.ManyToManyField(Especialidad, related_name='quimicos_farmaceuticos')
    area_medica= models.ForeignKey(AreaMedica, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self) -> str:
        return self.user.username

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    sexo = models.CharField(max_length=10)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    fecha_de_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='perfiles', blank=True, null=True)
    def __str__(self) -> str:
        return self.usuario.username
    

    


#Tablas de chat

class Chat(models.Model):
    dialogId = models.TextField()

class UsusariosChat(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_quimico = models.ForeignKey(QuimicoFarmaceutico, on_delete=models.CASCADE)
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)