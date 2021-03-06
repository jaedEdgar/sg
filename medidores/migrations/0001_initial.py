# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=250)),
                ('dias', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=250)),
                ('modelo', models.CharField(default='demo', max_length=250, null=True)),
                ('version_fw', models.CharField(default=True, max_length=250)),
                ('num_medidor', models.CharField(max_length=20, unique=True)),
                ('clave_pac', models.CharField(default=True, max_length=250)),
                ('punto', models.CharField(default=True, max_length=250)),
                ('radio', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='unidades.Radio')),
                ('unidad_consumo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unidades.UnidadConsumos')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumo', models.CharField(max_length=250)),
                ('status_ultima_lectura', models.CharField(choices=[('AB', 'Abierto'), ('CR', 'Cerrado')], max_length=3)),
                ('fecha_ultima_lectura', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('status_os', models.CharField(default='EnProceso', max_length=9, null=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('medidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medidores.Medidor')),
            ],
        ),
    ]
