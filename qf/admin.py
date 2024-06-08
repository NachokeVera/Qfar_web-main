from django.contrib import admin

# Register your models here.

from .models import Paciente, QuimicoFarmaceutico, Perfil, Especialidad,AreaMedica

admin.site.register(Paciente)
admin.site.register(QuimicoFarmaceutico)
admin.site.register(Perfil)
admin.site.register(Especialidad)
admin.site.register(AreaMedica)