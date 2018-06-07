# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from unidades.models import Radio,UnidadConsumos, Direccion
# Create your models here.


class Medidor(models.Model):
	tag = models.CharField(max_length=250)
	modelo = models.CharField(max_length=250,null=True,default='demo')
	version_fw= models.CharField(max_length=250,default=True)
	num_medidor = models.CharField(max_length=20,unique=True)
	clave_pac= models.CharField(max_length=250,default=True)
	punto= models.CharField(max_length=250,default=True)
	radio=models.ForeignKey(Radio,default=True)
	unidad_consumo = models.ForeignKey(UnidadConsumos,null=True)

class OrdenServicio(models.Model):
	LECTURA = (
		('AB','Abierto'),
		('CR','Cerrado')
		)
	STATUS = (
		('EP','EnProceso'),
		('PU','Pausada'),
		('AB','Abortada'),
		('CM','Completada'),
		('DS','Desconocido')
		)

	consumo = models.CharField(max_length=250)
	status_ultima_lectura= models.CharField(choices=LECTURA,max_length=3)
	fecha_ultima_lectura = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	status_os = models.CharField(default='EnProceso', null=True,max_length=9)
	descripcion = models.CharField(max_length=250)
	medidor = models.ForeignKey(Medidor,null=True)


class Grafica(models.Model):
	registro=models.CharField(max_length=250)
	dias = models.CharField(max_length=50)
