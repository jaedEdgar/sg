"""sg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from base.views import *

from medidores.views import *
from unidades.views import *

from medidores.views import *
from unidades.views import *

from django.views.generic.base import TemplateView
from django.conf.urls import handler404
from base.views import handler404,handler500
from django.conf import settings
from django.conf.urls.static import static
handler404 = 'base.views.handler404'
handler500 = 'base.views.handler500'


urlpatterns = [
	url(r'^$', index ,name='home'),
    url(r'^usuarios/$', lista_usuarios ,name='list_user'),
    url(r'^admin/', admin.site.urls),   
    url(r'^login/$', auth_views.login, {'template_name': 'base/login.html'}, name='login'),
    url(r'^user/new/$', add_user, name='add_user'),
    url(r'^user/edit/(?P<pk>\d+)/$', edit_user, name='edit_user'),
    url(r'^user/delete/(?P<pk>\d+)/$', delete_user, name='delete_user'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    #medidores
    url(r'^medidores/$', lista_medidores ,name='lista_medidores'),
    url(r'^medidores/agregar/$', add_medidores ,name='add_medidor'),
    url(r'^medidores/editar/(?P<pk>\d+)/$', edit_medidores ,name='edit_medidor'),
    url(r'^medidores/eliminar/(?P<pk>\d+)/$', delete_medidor ,name='delete_medidor'),

    #unidades
    url(r'^unidades/$', lista_unidades ,name='lista_unidades'),
    url(r'^agregar_unidad/$', add_unidad ,name='add_unidad'),

    #direcciones
    url(r'^direcciones/$', lista_direcciones ,name='lista_direccion'),
   # url(r'^agregar_direcciones/$', add_direcciones ,name='add_direcciones'),

    #Radios
    url(r'^radios/$', lista_radios ,name='lista_radio'),
    url(r'^agregar_radios/$', add_radios ,name='add_radio'),
    url(r'^radio_detalle/(?P<pk>\d+)/$', radio_detalle ,name='radio_detalle'),
    url(r'^unidad_consumo/$', add_unidadConsumo ,name='add_unidadConsumo'),
    url(r'^detalle_unidad/(?P<pk>\d+)/$', detalle_unidad ,name='detalle_unidad'),
    url(r'^radio/edit/(?P<pk>\d+)/$', edit_radio, name='edit_radio'),
    url(r'^radio/delete/(?P<pk>\d+)/$', delete_radio, name='delete_radio'),
    
    #orden de servicio
    url(r'^agregar_orden/$', orden_servicio ,name='orden_servicio'),
    url(r'^lista_ordenes/$', lista_os , name='lista_orden'),
    #apis
   url(r'^api/', include('apis.urls', namespace='api')),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)