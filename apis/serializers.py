from rest_framework import serializers
from unidades.models import *
from medidores.models import *


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class RClaveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Radio
		fields = ['clave']

class NMedidorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medidor
		fields = ['num_medidor']