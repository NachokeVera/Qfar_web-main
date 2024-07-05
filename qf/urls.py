from django.urls import path

from .views import home,nuevo_paciente,modificarP,inicio_sesion,inicio_admin,update_paciente,create_paciente,perfil,nuevo_quimico,perfilQ, quimicos_admin, index,login,listado,cerrarsesion,create_quimi_far,register,pacientes_admin,paciente_index, paciente_espera,quimico_chat,lista_pacientes_espera

urlpatterns = [
    path("index", index, name="index"),
    path('home', home, name='home'),
    path('login', login, name='login'),
    path('', inicio_sesion, name='inicio_sesion'),
    path('inicio_admin', inicio_admin, name='inicio_admin'),
    #Ruta para registrarse como paciente
    path('register', register, name='register'),
    path('perfil<int:id>', perfil, name='perfil'),
    path('perfilQ<int:id>', perfilQ, name='perfilQ'),
    path('create_paciente', create_paciente, name='createpaciente'),
    path('update_paciente', update_paciente, name='update_paciente'),
    path('listado', listado, name='listado'),
    path('modificarP<int:id>', modificarP, name='modificarP'),
    path('cerrarsesion', cerrarsesion, name='cerrarsesion'),
    path('nuevo_paciente', nuevo_paciente, name='nuevo_paciente'),
    path('nuevo_quimico', nuevo_quimico, name='nuevo_quimico'),
    path('pacientes_admin', pacientes_admin, name='pacientes_admin'),
    path('quimicos_admin', quimicos_admin, name='quimicos_admin'),
    #Ruta para registrar un quimico farmaceutico
    path('form', create_quimi_far, name='adminform'),
    #rutas paciente
    path('paciente/index',paciente_index, name='paciente_index'),
    path('paciente/espera',paciente_espera, name='paciente_espera'),
    #rutas quimico farmaceutico
    path('quimicofar/chat/<int:user_id>',quimico_chat, name='quimico_chat'),
    path('quimicofar/lista/espera',lista_pacientes_espera, name='lis_pac_esp'),
]
