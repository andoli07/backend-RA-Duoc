from rest_framework import serializers
from .models import Residente

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residente
        fields = ['rut', 'nombre', 'correo', 'rol', 'unidad']

    def create(self, validated_data):
        return Residente.objects.create(**validated_data)