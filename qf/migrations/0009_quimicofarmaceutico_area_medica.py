# Generated by Django 5.0.6 on 2024-06-08 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qf', '0008_especialidad_alter_areamedica_area_medica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quimicofarmaceutico',
            name='area_medica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qf.areamedica'),
        ),
    ]
