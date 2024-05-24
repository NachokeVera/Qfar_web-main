# Generated by Django 5.0.6 on 2024-05-19 01:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qf', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_medica', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='esperando',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=1)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('telefono', models.CharField(max_length=15, unique=True)),
                ('fecha_de_nacimiento', models.DateField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
