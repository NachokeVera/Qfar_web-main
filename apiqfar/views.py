from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from qf.models import Paciente,Especialidad,Enfermedad
from .serializer import PacienteSerializer, PatologiasSerializer,EnfermedadSerializar
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
def getData(request):
    pacientes = Paciente.objects.all()
    if pacientes.exists():
        serializer = PacienteSerializer(pacientes, many=True)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 404, 'message': 'No se encontraron pacientes.'}, status=status.HTTP_404_NOT_FOUND)




class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class especialidadesList(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = PatologiasSerializer


class CrearPacienteView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            paciente = serializer.save()
            return Response({'id': paciente.usuario.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CrearEnfermedad(APIView):
    def post(self, request, format=None):
        serializer = EnfermedadSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CrearUsuarioView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    correo = request.data.get('correo')
    clave = request.data.get('clave')
    user = authenticate(request, username=correo, password=clave)

    if user is not None:
        # Suponiendo que tienes un modelo Usuario extendido
        usuario_data = {
            'id': user.id,
            'rol': user.usuario.rol,  # Ajusta esto según tu modelo
            'idioma': user.usuario.idioma,  # Ajusta esto según tu modelo
            'idasignatura': user.usuario.idasignatura if user.usuario.rol == '2' else None  # Ajusta esto según tu modelo
        }
        return JsonResponse(usuario_data)
    else:
        return JsonResponse({'error': 'Credenciales incorrectas'}, status=400)

@api_view(['GET'])
def logout(request):
    return Response({})


@api_view(['POST'])
def register(request):

    user_data = request.data.get('user', {})
    paciente_data = request.data.get('paciente', {})

    user_serializer = UserSerializer(data=user_data)
    paciente_serializer = PacienteSerializer(data=paciente_data)

    if user_serializer.is_valid() and paciente_serializer.is_valid():
        user = user_serializer.save()
        paciente_data['user'] = user
        paciente = Paciente.objects.create(**paciente_data)

        user.save()
        paciente.save()
        token = Token.objects.create(user=user)
        


        return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_201_CREATED)
        
    return Response(user_serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def porfile(request):
    return Response({})

@api_view(['POST'])
def verify(request):
    username = request.data.get('username')
    token_key = request.data.get('token')

    if not username or not token_key:
        return Response({'error': 'Username and token are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
        token = Token.objects.get(user=user)

        if token.key == token_key:
            return Response({'result': 'success','uid': user.id}, status=status.HTTP_200_OK)
        else:
            return Response({'result': 'failure'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Token.DoesNotExist:
        return Response({'error': 'Token does not exist'}, status=status.HTTP_404_NOT_FOUND)