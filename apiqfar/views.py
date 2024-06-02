from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from qf.models import Paciente
from .serializer import PacienteSerializer

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
    return Response({})

@api_view(['GET'])
def logout(request):
    return Response({})


@api_view(['POST'])
def register(request):
    return Response({})

@api_view(['GET'])
def porfile(request):
    return Response({})
