# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from medidores.models import *
from django.views.defaults import page_not_found


def handler404(request):
    response = render_to_response('base/404.html', {'exception': ex},
    context_instance=RequestContext(request), status=404)
    
    return response
def handler500(request):
    return render(request, 'base/404.html', status=500)

@login_required
def index(request):
		if	request.user.is_superuser:
			grafica = Grafica.objects.all()
			return  render(request,'base/index.html',{'grafica':grafica})
		else:
			return HttpResponseNotFound('<h1>Page not found</h1>')


def lista_usuarios(request):
	if	request.user.is_superuser:
		usuarios = User.objects.all().filter(is_active=True)
		return  render(request,'usuarios/lista_usuarios.html',{'usuarios':usuarios})

	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')


def add_user(request):
	if request.method == 'POST':
		tipo = request.POST.get('tipo')
		usuario =  request.POST.get('usuario')
		password =  request.POST.get('password')
		first_name = request.POST.get('nombre')
		last_name = request.POST.get('apellidos')
		email = request.POST.get('email')
		if request.POST.get('id'):
			user = User.objects.get(id=int(request.POST.get('id')))
			user.username = usuario
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.is_superuser = tipo
			if len(password) > 0 :
				user.set_password(password)
			user.save()
			return  redirect('/usuarios/')
		else:
			if int(tipo) == 1:
				User.objects.create_superuser(username=usuario, password=password,email=email,last_name=last_name,first_name=first_name)
			else:
				User.objects.create_user(username=usuario, password=password,email=email,last_name=last_name,first_name=first_name)
			return  redirect('/usuarios/')
	else:

		return render(request,'usuarios/add-user.html')



def edit_user(request,pk):
	usuario = User.objects.get(id=pk)
	env = {
		'usuario':usuario,
	}

	return render(request,'usuarios/add-user.html',env)




def delete_user(request,pk):
	usuario = User.objects.get(id=pk)
	usuario.is_active= False
	usuario.save()

	return  redirect('/usuarios/')



