from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from qf.models import Paciente
from .serializer import PacienteSerializer
from .serializer import UserSerializer
from django.contrib.auth.models import User
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





@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

    token,created = Token.objects.get_or_create(user=user)
    print(token)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key,'user':serializer.data}, status=status.HTTP_200_OK)

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