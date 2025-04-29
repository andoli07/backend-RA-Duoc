from django.urls import path
from .views import hello_api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from administracion.models import Residente
from .views import registro_residente
from administracion import views


def ver_registros(request):
    registros = list(Residente.objects.values())
    return JsonResponse(registros, safe=False)

urlpatterns = [
    path('api/hello/', hello_api, name='hello_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/registro/residente/', registro_residente, name='registro_residente'),
    path('api/registros/', ver_registros),
    path('api/csrf/', views.csrf, name='csrf'),
]