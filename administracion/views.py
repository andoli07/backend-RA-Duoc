from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResidenteSerializer

class RegistrarUsuario(APIView):
    def post(self, request):
        serializer = ResidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario creado'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
