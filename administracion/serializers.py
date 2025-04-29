# serializers.py
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from administracion.models import Residente, Rol, UnidadHabitacional
from django.core.exceptions import ValidationError
import re


class ResidenteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    unidad = serializers.PrimaryKeyRelatedField(
        queryset=UnidadHabitacional.objects.all(),
        required=True
    )

    class Meta:
        model = Residente
        fields = ['rut', 'nombre', 'correo', 'password', 'unidad']

    def validate_rut(self, value):
        # Validación básica de RUT chileno
        if not re.match(r'^\d{7,8}-[\dkK]$', value):
            raise ValidationError("Formato de RUT inválido. Debe ser: 12345678-9")
        return value

    def create(self, validated_data):
        # Asignar rol automáticamente
        validated_data['rol'] = Rol.objects.get_or_create(tipo='residente')[0]
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)