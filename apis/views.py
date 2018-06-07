# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import  ListCreateAPIView,ListAPIView
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import *


class MunicipioApi(APIView):
    def get(self,request,*args,**kwargs):
        estado= self.kwargs.get('estado')

        municipios = Municipio.objects.filter(estado=estado)
        serializer = MunicipioSerializer(municipios,many=True)
        return Response(serializer.data)

class RadioApi(APIView):
	def get(self,request,*args,**kwargs):
		clave = self.kwargs.get('clave')
		radio = Radio.objects.get(clave=clave)
		serializer = RClaveSerializer(radio)
		return Response(serializer.data)

class MedidorApi(APIView):
	def get(self,request,*args,**kwargs):
		numero = self.kwargs.get('num_medidor')
		medidor = Medidor.objects.get(num_medidor=numero)
		serializer = NMedidorSerializer(medidor)
		return Response(serializer.data)