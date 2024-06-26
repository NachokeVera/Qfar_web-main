# Generated by Django 5.0.6 on 2024-05-12 21:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cesfam', models.CharField(max_length=40)),
                ('sintomas', models.TextField()),
                ('peso', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuimicoFarmaceutico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universidad', models.CharField(max_length=60)),
                ('titulo', models.CharField(max_length=60)),
                ('curriculum', models.TextField()),
                ('horario_disponible', models.CharField(max_length=60)),
                ('numero_registro', models.CharField(max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quimico_farmaceutico', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
