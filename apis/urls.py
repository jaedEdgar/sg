from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^municipio/(?P<estado>\w+)/$', MunicipioApi.as_view(), name='municipios'),
    url(r'^radio/(?P<clave>\w+)/$', RadioApi.as_view(), name='clave'),
	url(r'^medidor/(?P<num_medidor>\w+)/$', MedidorApi.as_view(), name='medidor'),
]