from django.urls import path

from .views import home,nuevo_paciente, quimicos_admin, index,login,listado,cerrarsesion,create_quimi_far,register,pacientes_admin,paciente_index, paciente_espera,quimico_chat,lista_pacientes_espera

urlpatterns = [
    path("index", index, name="index"),
    path('home', home, name='home'),
    path('login', login, name='login'),
    #Ruta para registrarse como paciente
    path('register', register, name='register'),
    path('listado', listado, name='listado'),
    path('cerrarsesion', cerrarsesion, name='cerrarsesion'),
    path('nuevo_paciente', nuevo_paciente, name='nuevo_paciente'),
    path('pacientes_admin', pacientes_admin, name='pacientes_admin'),
    path('quimicos_admin', quimicos_admin, name='quimicos_admin'),
    #Ruta para registrar un quimico farmaceutico
    #path('admin/form', create_quimi_far, name='adminform'),
    #rutas paciente
    path('paciente/index',paciente_index, name='paciente_index'),
    path('paciente/espera',paciente_espera, name='paciente_espera'),
    #rutas quimico farmaceutico
    path('quimicofar/chat/<int:user_id>',quimico_chat, name='quimico_chat'),
    path('quimicofar/lista/espera',lista_pacientes_espera, name='lis_pac_esp'),
]
