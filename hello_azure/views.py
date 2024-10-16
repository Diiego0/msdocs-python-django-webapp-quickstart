from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Calificacion
from .serializers import CalificacionSerializer

def index(request):
    print('Request for index page received')
    return render(request, 'stats/index.html')

def mostrar_calificaciones(request):
    # Obtener todas las calificaciones
    calificaciones = Calificacion.objects.all()

    # Pasar las valoraciones a la plantilla
    return render(request, 'stats/calificaciones.html', {'calificaciones': calificaciones})

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

