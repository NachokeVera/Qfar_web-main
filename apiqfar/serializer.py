from rest_framework import serializers
from django.contrib.auth.models import User
from qf.models import Paciente,Usuario, Especialidad,Enfermedad

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nombre_usuario', 'correo', 'clave', 'sexo', 'rut', 'telefono', 'fecha_de_nacimiento']

class PacienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Paciente
        fields = ['id','cesfam', 'sintomas', 'peso', 'esperando', 'usuario', 'patologias']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        patologias_data = validated_data.pop('patologias')
        usuario = Usuario.objects.create(**usuario_data)
        paciente = Paciente.objects.create(usuario=usuario, **validated_data)
        paciente.patologias.set(patologias_data)  
        return paciente
    
class EnfermedadSerializar(serializers.ModelSerializer):
  

    class Meta:
        model = Enfermedad
        fields = ['id', 'nombre', 'pato', 'medicamentos', 'usuario']

    def create(self, validated_data):
        
        enfermedad = Enfermedad.objects.create( **validated_data)
        return enfermedad
    
class PatologiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id','especialidad']
   