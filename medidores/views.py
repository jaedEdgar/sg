# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from unidades.models import *
from medidores.models import *
# Create your views here.



#Medidores
def lista_medidores(request):
	if	request.user.is_superuser:
		medidores = Medidor.objects.all()
		return  render(request,'medidores/lista_medidores.html',{'medidores':medidores})
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')

def add_medidores(request):
	if request.method == 'POST':
		num_medidor =request.POST.get('num_medidor')
		tag_medidor = request.POST.get('tag_medidor')
		modelo= request.POST.get('modelo')
		version_fw=request.POST.get('version_fw')
		clave_pac = request.POST.get('clave_pac')
		punto=request.POST.get('punto')
		radio_id = request.POST.get('radio')
		if request.POST.get('medidor_id'):
			medidor = Medidor.objects.get(id=request.POST.get('medidor_id'))
			medidor.num_medidor = num_medidor
			medidor.tag=tag_medidor
			medidor.radio_id=radio_id
			medidor.modelo=modelo
			medidor.version_fw=version_fw
			medidor.clave_pac=clave_pac
			medidor.save()
			return redirect('/medidores/')
		else:
			medidores= Medidor(num_medidor=num_medidor, tag=tag_medidor, radio_id=radio_id,modelo=modelo,version_fw=version_fw,clave_pac=clave_pac)
			medidores.save()
			return redirect('/medidores/')
	else:
		radios = Radio.objects.all()
		return render(request,'medidores/add_medidores.html',{'radios':radios}	)

def edit_medidores(request,pk):
	medidor = Medidor.objects.get(id=pk)
	radios = Radio.objects.all()
	env = {
		'medidor':medidor,
		'radios':radios
	}

	return render(request,'medidores/add_medidores.html',env)

	
def delete_medidor(request,pk):
	Medidor.objects.get(id=pk).delete()
	return redirect('/medidores/')
#Ordenes de Servicio
def orden_servicio(request):
	if request.method == 'POST':
		consumo = request.POST.get('consumo')
		status_ultima_lectura=request.POST.get('status')
		fecha_ultima_lectura=request.POST.get('fecha')
		is_active=request.POST.get('os')
		descripcion =request.POST.get('descripcion')

		orden = OrdenServicio(consumo=consumo,status_ultima_lectura=status_ultima_lectura,fecha_ultima_lectura=fecha_ultima_lectura,is_active=is_active,descripcion=descripcion)
		orden.save()
		return redirect('/lista_ordenes/')
	else:
		medidores = Medidor.objects.all()
		orden = OrdenServicio.LECTURA
		
		env={
		'orden':orden,
		'medidores':medidores,
		}
		return render(request,'unidades/orden_servicio/add_orden_servicio.html',env)


def lista_os(request):

	orden_servicio= OrdenServicio.objects.all()
	user = User.objects.all().filter(is_active=True)
	env = {

	'orden_servicio':orden_servicio,
	'user':user,

	}
	return render (request,'unidades/orden_servicio/list_orden_servicio.html',env)
