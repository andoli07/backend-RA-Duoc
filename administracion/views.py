from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Residente
from .serializers import ResidenteSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie



@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hola desde Django API!"})

@csrf_exempt
@api_view(['POST'])
def registro_residente(request):
    response = Response()
    response["Access-Control-Allow-Origin"] = "https://obscure-parakeet-6947wx6vv96xfx49q-5173.app.github.dev"
    response["Access-Control-Allow-Credentials"] = "true"
    
    try:
        serializer = ResidenteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response.data = serializer.data
        response.status_code = 201
    except Exception as e:
        response.data = {'error': str(e)}
        response.status_code = 400
    
    return response

@ensure_csrf_cookie
def csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['Access-Control-Allow-Origin'] = "https://obscure-parakeet-6947wx6vv96xfx49q-5173.app.github.dev"
    response['Access-Control-Allow-Credentials'] = 'true'
    return response

class RegistroResidenteView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer