from django.contrib import admin

# Register your models here.

from .models import Paciente, QuimicoFarmaceutico

admin.site.register(Paciente)
admin.site.register(QuimicoFarmaceutico)