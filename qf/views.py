from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, logout,login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os


from django.core.exceptions import ObjectDoesNotExist
from .models import Paciente, QuimicoFarmaceutico, UsusariosChat, Chat, Perfil
from .connectycube import create_session,register_user_connecticube,search_user,create_dialog

# Create your views here.

def index(request):
    return HttpResponse("hellow, world")

def inicio_admin(request):

    paciente=Paciente.objects.all()
    total_pacientes= paciente.count()
    quimico=QuimicoFarmaceutico.objects.all()
    total_quimicos= quimico.count()

    context = {
        'UsuarioSistema': paciente,
        'totalP': total_pacientes,
        'totalQ': total_quimicos

        }
    return render(request,'adminn/inicio.html',context)

def perfil(request,id):
    paciente=Paciente.objects.get(user__id=id)
    perfilP=Perfil.objects.get(usuario__id=id)
    
    context = {'perfil': paciente,
               'perfilP': perfilP}
    return render(request,'adminn/perfil.html',context)
def perfilQ(request,id):
    quimico=QuimicoFarmaceutico.objects.get(user__id=id)
    perfilP=Perfil.objects.get(usuario__id=id)
    
    context = {'perfil': quimico,
               'perfilQ': perfilP}
    return render(request,'adminn/perfilQ.html',context)

def pacientes_admin(request):
    paciente=Paciente.objects.all()
    context = {'UsuarioSistema': paciente }
    return render(request,'adminn/pacientes.html',context)

def quimicos_admin(request):
    quimico=QuimicoFarmaceutico.objects.all()
    context = {'quimicoSistema': quimico }
    return render(request,'adminn/quimicos.html',context)

def nuevo_paciente(request):
    quimico=QuimicoFarmaceutico.objects.all()
    context = {'quimicoSistema': quimico }
    return render(request,'adminn/nuevo_paciente.html',context)

def home(request):
    return render(request,'qf/home.html')

def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        user = authenticate(username=usuario, password=contrasena)
        if user is not None:
            auth_login(request, user)
            token = create_session(usuario,contrasena)
            print(token)
            request.session['tokenUser'] = token
            return redirect('paciente_index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')
    else:
        return render(request,'login.html')

def listado(request):
    vCorreo = request.user.username

    contexto={
        "datos": vCorreo,
        
    }
    return render(request,'qf/listado.html',contexto)

def cerrarsesion(request):
    if 'tokenUser' in request.session:
        del request.session['tokenUser']
    logout(request)
    return redirect('login')

def create_quimi_far(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('contrasena')
        universidad = request.POST.get('universidad')
        sexo = request.POST.get('sexo')
        rut = request.POST.get('rut')
        telefono = request.POST.get('telefono')
        fechanac = request.POST.get('fecha_nac')
        titulo = request.POST.get('titulo')
        foto = request.FILES['foto']
        curriculum = request.POST.get('curriculum')
        numero_registro = request.POST.get('numero_registro')
        horario_disponible = request.POST.get('hora_disponible')

        # Crear el usuario de Django
        user = User.objects.create_user(username, email, password)
        user.save()

        # Crear el objeto QuimicoFarmaceutico relacionado
        perfil = Perfil.objects.create(
             usuario=user,
             sexo =sexo,
             foto=foto,
             rut = rut,
             telefono =telefono,
             fecha_de_nacimiento = fechanac

        )
        quimico_farmaceutico = QuimicoFarmaceutico.objects.create(
            user=user,
            universidad=universidad,
            titulo=titulo,
            curriculum=curriculum,
            numero_registro=numero_registro,
            horario_disponible=horario_disponible
        )
        quimico_farmaceutico.save()
        perfil.save()

        token = create_session()
        register_user_connecticube(token, username, email, password)

        return redirect('inicio_admin')
    else:
        return render(request,'adminn/formulario_qf.html')
    
def create_paciente(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        password = request.POST.get('clave')
        sexo = request.POST.get('sexo')
        rut = request.POST.get('rut')
        foto = request.FILES['foto']
        telefono = request.POST.get('telefono')
        fechanac = request.POST.get('fecha_nac')
        cesfam= request.POST.get('cesfam')
        
        sintomas= request.POST.get('telefono')
        peso= request.POST.get('peso')
      
       
       

        # Crear el usuario de Django
        user = User.objects.create_user(username, email, password)
        user.save()

        # Crear el objeto QuimicoFarmaceutico relacionado
        perfil = Perfil.objects.create(
             usuario=user,
             sexo =sexo,
             foto= foto,
             rut = rut,
             telefono =telefono,
             fecha_de_nacimiento = fechanac

        )
        paciente = Paciente.objects.create(
            user=user,
            cesfam=cesfam,
            sintomas=sintomas,
            peso=peso

           
        )
        paciente.save()
        perfil.save()
        auth_login(request, user) 
        token = create_session()
        connectycube_user = register_user_connecticube(token, username, email, password)
        print(token)

        return redirect('inicio_admin')
    else:
        return render(request,'adminn/nuevo_paciente.html')
    
def register(request):
    if request.method == 'POST':
        v_username = request.POST.get('usuario')
        v_email = request.POST.get('email')
        v_password = request.POST.get('contrasena')
        v_cesfam = request.POST.get('cesfam')
        v_sint = request.POST.get('sintomas')
        v_peso =request.POST.get('peso')
        # Crear el usuario de Django
        user = User.objects.create_user(v_username, v_email, v_password)
        user.save()
        

        # Crear el objeto QuimicoFarmaceutico relacionado
        paciente = Paciente.objects.create(
            user=user,
            cesfam = v_cesfam,
            sintomas = v_sint,
            peso = v_peso
  
        )
        paciente.save()
        auth_login(request, user) 
        token = create_session()
        connectycube_user = register_user_connecticube(token, v_username, v_email, v_password)
        print(token)
        return redirect('paciente_index')
    else:

        return render(request,'register.html')
    
def paciente_index(request):
    
    current_user = request.user.username
    context = {
        'data' : current_user,
    }
    return render(request, 'paciente/index.html',context)

def paciente_espera(request):
    def usuario_chat_exist(paciente):
        try:
            usuariosChat = UsusariosChat.objects.get(id_paciente = paciente.id)
            return usuariosChat
        except UsusariosChat.DoesNotExist:
            return False

    user = request.user
    paciente = Paciente.objects.get(user_id = user.id)
    usuarioChat = usuario_chat_exist(paciente)

    if usuarioChat:
        #rescatar id paciente y token
        token = request.session['tokenUser']
        responsePac = search_user(token, user.username)
        idPac = responsePac['items'][0]['id']
        #rescatar dialog para conectarme a conectycube
        chat = Chat.objects.get(id = usuarioChat.id_chat.id)
        dialogId = chat.dialogId
        context = {
            'token': token,
            'user_id_connectycube': idPac,
            'dialogId': dialogId
        }
        return render(request, 'paciente/chat.html',context)
    
    paciente.esperando = True
    paciente.save()
    context = {
        'user' : user,
    }
    return render(request, 'paciente/espera.html',context)

def lista_pacientes_espera(request):

    pac_espera_list = Paciente.objects.filter(esperando=True)
    user_data = []
    for i in pac_espera_list:
        user = User.objects.get(id = i.user_id)
        user_data.append(user)

    context = {
        #'pacientes_espera': pac_espera_list,
        'user_data': user_data
    }

    return render(request, 'qf/lista_pac_espera.html',context)

def quimico_chat(request, user_id):
    #contiene a los usuarios del chat
    chat_user = []
    #aqui obtengo el token del usuario, en este caso deberia ser el quimico far
    token = request.session['tokenUser']
    #info del paciente con el cual creara el chat
    paciente = Paciente.objects.get(user_id = user_id)
    quimico = QuimicoFarmaceutico.objects.get(user_id = request.user.id)
    user = User.objects.get(id = user_id)
    #response para el paciente
    responsePac = search_user(token, user.username)
    idPac = responsePac['items'][0]['id']
    #responde del quimicoFar (el request contiene informacion del usuario logeado)
    responseQui = search_user(token, request.user.username)
    idQui = responseQui['items'][0]['id']

    chat_user.append(idPac)
    chat_user.append(idQui)

    dialog_response = create_dialog(token,chat_user)
    dialogID = dialog_response['_id']
    paciente.esperando = False
    paciente.save()
    #creo un objeto que contendra a los usuarios, posterior mente subire a la base de datos
    chat = Chat.objects.create(dialogId = dialogID)
    usuarios_chat = UsusariosChat.objects.create(id_paciente = paciente, id_quimico = quimico, id_chat = chat)
    usuarios_chat.save()
    context = {
        'token': token,
        'user_id_connectycube': idQui,
        'dialogId': dialogID,
    }
    return render(request, 'qf/chat_qf.html',context)