from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, logout,login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Paciente, QuimicoFarmaceutico, UsusariosChat, Chat
from .connectycube import create_session,register_user_connecticube,search_user,create_dialog_private

# Create your views here.

def index(request):
    return HttpResponse("hellow, world")

def pacientes_admin(request):
    paciente=Paciente.objects.all()
    context = {'UsuarioSistema': paciente }
    return render(request,'admin/pacientes.html',context)

def quimicos_admin(request):
    quimico=QuimicoFarmaceutico.objects.all()
    context = {'quimicoSistema': quimico }
    return render(request,'admin/quimicos.html',context)

def nuevo_paciente(request):
    quimico=QuimicoFarmaceutico.objects.all()
    context = {'quimicoSistema': quimico }
    return render(request,'admin/nuevo_paciente.html',context)

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
        titulo = request.POST.get('titulo')
        curriculum = request.POST.get('curriculum')
        numero_registro = request.POST.get('numero_registro')
        horario_disponible = request.POST.get('hora_disponible')

        # Crear el usuario de Django
        user = User.objects.create_user(username, email, password)
        user.save()

        # Crear el objeto QuimicoFarmaceutico relacionado
        quimico_farmaceutico = QuimicoFarmaceutico.objects.create(
            user=user,
            universidad=universidad,
            titulo=titulo,
            curriculum=curriculum,
            numero_registro=numero_registro,
            horario_disponible=horario_disponible
        )
        quimico_farmaceutico.save()

        token = create_session()
        register_user_connecticube(token, username, email, password)

        return redirect('index')
    else:
        return render(request,'admin/formulario_qf.html')
    
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
    user = request.user
    paciente = Paciente.objects.get(user_id = user.id)

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

    dialog_response = create_dialog_private(token,chat_user)
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