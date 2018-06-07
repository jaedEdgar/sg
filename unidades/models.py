# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Municipio(models.Model):
	ESTADOS = (
		('AGS', 'Aguascalientes'),
		('BC', 'Baja California'),
		('BCS', 'Baja California Sur'),
		('CAM', 'Campeche'),
		('CHP', 'Chiapas'),
		('CHI', 'Chihuahua'),
		('DIF', 'Ciudad de México'),
		('COA', 'Coahuila'),
		('COL', 'Colima'),
		('DUR', 'Durango'),
		('GTO', 'Guanajuato'),
		('GRO', 'Guerrero'),
		('HGO', 'Hidalgo'),
		('JAL', 'Jalisco'),
		('MEX', 'México'),
		('MIC', 'Michoacán'),
		('MOR', 'Morelos'),
		('NAY', 'Nayarit'),
		('NLE', 'Nuevo León'),
		('OAX', 'Oaxaca'),
		('PUE', 'Puebla'),
		('QRO', 'Querétaro'),
		('ROO', 'Quintana Roo'),
		('SLP', 'San Luis Potosí'),
		('SIN', 'Sinaloa'),
		('SON', 'Sonora'),
		('TAB', 'Tabasco'),
		('TAM', 'Tamaulipas'),
		('TLX', 'Tlaxcala'),
		('VER', 'Veracruz'),
		('YUC', 'Yucatán'),
		('ZAC', 'Zacatecas')
	)
	nombre = models.CharField(max_length=255)
	estado = models.CharField(choices=ESTADOS, max_length=3)

class Direccion(models.Model):
	calle = models.CharField(max_length=255)
	numero = models.IntegerField()
	colonia = models.CharField(max_length=255)
	codigo_postal= models.CharField(max_length=10)
	municipio = models.ForeignKey(Municipio)
	longitud = models.CharField(max_length=240)
	latitud = models.CharField(max_length=240)

class Radio (models.Model):
	clave = models.CharField(max_length=6,unique=True)
	tag_radio = models.CharField(max_length=255)
	modelo = models.CharField(max_length=250,null=True,default=True)
	version_fw = models.CharField(max_length=250,null=True,default=True)
	protocolo = models.CharField(max_length=250,null=True,default=True)
	direccion = models.ForeignKey(Direccion)


class UnidadConsumos(models.Model):
	unidad_consumo = models.CharField(max_length=60)
	tag_unidad_consumo = models.CharField(max_length=255)
	radio = models.ForeignKey(Radio, null=True)


class Unidad(models.Model):
	ubicacion = models.ForeignKey(Direccion,null=True)
	status_unidad = models.BooleanField(default=True)
	status_comunicacion_unidad=models.BooleanField(default=True)
	status_conecxion = models.BooleanField(default=True)