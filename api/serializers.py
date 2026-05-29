from rest_framework import serializers
from .models import Emisora


class EmisoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emisora
        fields = ['id', 'titulo', 'cadena', 'ciudad', 'url', 'via', 'codename']
