from django.urls import path,re_path
from . import views
from django.urls import path
from .views import PacienteList, CrearPacienteView,CrearUsuarioView,especialidadesList,login,CrearEnfermedad

urlpatterns = [
    path('', views.getData), 
    re_path('login',views.login),
    re_path('register',views.register),
    re_path('verify',views.verify),
    path('pacientes/', PacienteList.as_view(), name='paciente-list'),
    path('patologias/', especialidadesList.as_view(), name='especialidades-list'),
    path('crear_paciente/', CrearPacienteView.as_view(), name='crear_paciente'),
    path('crear_enfermedad/', CrearEnfermedad.as_view(), name='crear_enfermedad'),
    path('crear_usuario/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('login/', login, name='login'),
]