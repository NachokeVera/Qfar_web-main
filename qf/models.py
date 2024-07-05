from django.contrib.auth.models import User

from django.db import models

#Modelos correspondientes a los tipos de usuarios
class Especialidad(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id de la especialidad')
    especialidad= models.CharField(max_length=20, verbose_name='nombre de la especialidad', null=False, blank=False)

    def __str__(self) -> str:
        return self.especialidad
class Usuario(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id del usuario')
    nombre_usuario=models.CharField(max_length=20, verbose_name='nombre del usuario', null=False, blank=False)
    correo= models.CharField(max_length=25, verbose_name='ingresa un correo', null=False, blank=False)
    clave=models.CharField(max_length=16,  verbose_name='ingresa una contraseña', null=False, blank=False)
    sexo = models.CharField(max_length=10)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    fecha_de_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='usuarios', blank=True, null=True)
   
   
    def __str__(self) -> str:
        return self.nombre_usuario
class Paciente(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id del paciente')
    cesfam = models.CharField(max_length=40)
    sintomas = models.TextField()

    peso = models.IntegerField()
    esperando = models.BooleanField(default=False)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE,blank=True, null=True)
    patologias = models.ManyToManyField(Especialidad, related_name='paciente')
   
    def __str__(self) -> str:
        return self.usuario.nombre_usuario
    

    
class Enfermedad(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='id de la enfermedad')
    nombre = models.CharField(max_length=40)
    pato= models.ForeignKey(Especialidad, on_delete=models.CASCADE,blank=True, null=True)
    medicamentos = models.TextField()
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE,blank=True, null=True)
   
    def __str__(self) -> str:
        return self.nombre


    
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
    calificacion = models.IntegerField(blank=True, null=True, default=0)
    estado = models.BooleanField(default=False)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE,blank=True, null=True)
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