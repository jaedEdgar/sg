# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from unidades.models import *

# Create your views here.

#Direcciones
def lista_direcciones(request):
	if	request.user.is_superuser:
		direcciones = Direccion.objects.all()
		return  render(request,'unidades/direcciones/list_direcciones.html',{'direcciones':direcciones})
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')

'''def add_direcciones(request):
	if request.method == 'POST':
		calle =request.POST.get('calle')
		numero = request.POST.get('numero')
		colonia = request.POST.get('colonia')
		codigo_postal = request.POST.get('codigo_postal')
		municipio = int(request.POST.get('municipio'))
		longitud = request.POST.get('longitud')
		latitud = request.POST.get('latitud')

		direccion= Direccion(calle=calle, numero=numero, colonia=colonia, codigo_postal=codigo_postal,municipio_id=municipio,longitud=longitud,latitud=latitud )
		direccion.save()
		return redirect('/direcciones/')
	else:
		estados = Municipio.ESTADOS
		env = {
			'estados': estados,
		}
	return render(request,'unidades/direcciones/add_direcciones.html',env)
'''


#Radios
def lista_radios(request):
	#if	request.user.is_superuser:
		radios =Radio.objects.all()
		env={
			'radios':radios
		}
		return  render(request,'unidades/radios/list_radios.html',env)
	#else:
	#	return HttpResponseNotFound('<h1>Page not found</h1>')

def add_radios(request):
	if request.method == 'POST':
		clave= request.POST.get('radio_id')
		tag= request.POST.get('tag_radio')
		modelo=request.POST.get('modelo')
		version_fw=request.POST.get('version_fw')
		protocolo=request.POST.get('protocolo')
		calle =request.POST.get('calle')
		numero = request.POST.get('numero')
		colonia = request.POST.get('colonia')
		codigo_postal = request.POST.get('codigo_postal')
		municipio = int(request.POST.get('municipio'))
		longitud = request.POST.get('longitud')
		latitud = request.POST.get('latitud')
		if request.POST.get('id'):
			radio= Radio.objects.get(id=request.POST.get('id'))
			radio.clave = clave
			radio.tag_radio = tag
			radio.modelo = modelo
			radio.version_fw = version_fw
			radio.protocolo = protocolo
			radio.direccion.calle = calle
			radio.direccion.numero = numero
			radio.direccion.colonia = colonia
			radio.direccion.codigo_postal= codigo_postal
			radio.direccion.longitud= longitud
			radio.direccion.latitud= latitud
			radio.direccion.municipio_id = municipio
			radio.save()
			radio.direccion.save()
			return redirect('/radios/')
		else:
			direccion= Direccion(calle=calle,numero=numero,colonia=colonia,
								 codigo_postal=codigo_postal,
								 municipio_id=municipio,
								 longitud=longitud,
								 latitud=latitud )
			direccion.save()
			radio = Radio(clave=clave,tag_radio=tag,modelo=modelo,version_fw=version_fw,protocolo=protocolo,direccion=direccion)
			radio.save()
			return redirect('/radios')
	else:
		estados = Municipio.ESTADOS
		env = {
			'estados': estados,
		}
		return render(request,'unidades/radios/add_radios.html',env)

def edit_radio(request,pk):
	radio = Radio.objects.get(id=pk)

	estados = Municipio.ESTADOS
	env ={
		'radio':radio,
		'estados': estados,
	}
	return render (request,'unidades/radios/add_radios.html',env)

def delete_radio(request,pk):
	radio= Radio.objects.filter(id=pk).delete()
	return  redirect('/radios/')


def radio_detalle(request,pk):
	radio = Radio.objects.get(id=pk)
	direccion = Direccion.objects.get(id=radio.direccion_id)
	env={
		'radio':radio,
		'latitud':direccion.latitud,
		'longitud':direccion.longitud
	}
	return render(request,'unidades/radios/detalle_radio.html',env)



#unidad de consumo
def detalle_unidad(request,pk):
	radio = Radio.objects.get(id=pk)
	env ={
	'radio':radio
	}
	return render (request,'unidades/radios/unidad_consumo.html',env)

def add_unidadConsumo(request):
	if request.method == 'POST':
		unidad_consumo = request.POST.get('unidad_consumo')
		tag_unidad_consumo = request.POST.get('tag_unidad_consumo')
		radio_id = request.POST.get('radio_id')
		asig = UnidadConsumos(unidad_consumo=unidad_consumo,tag_unidad_consumo=tag_unidad_consumo,radio_id=radio_id)
		asig.save()
		return redirect('/radios')
	else:
		return render (request,'unidades/radios/unidad_consumo.html')



def lista_unidades(request):
	if	request.user.is_superuser:
		unidades = Unidad.objects.all()
		return  render(request,'unidades/lista_unidades.html',{'unidades':unidades})
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')


def add_unidad(request):
	if request.method == 'POST':
		if request.POST.get('id'):
			medidor = Medidores.objects.get(request.POST.get('id'))
			medidor.num_medidor = num_medidor
			medidor.acometida = acometida
			medidor.save()
		#if request.POST.get('id'):
		#medidor = Medidores.objects.get(id=int(request.POST.get('id')))
		#	medidor.num_medidor = num_medidor
		#	medidor.acometida = acometida
			return  redirect('lista_unidades')
	else:
			
			return render(request,'unidades/add_unidades.html')


