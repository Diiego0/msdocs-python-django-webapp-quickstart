from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'calificaciones', CalificacionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('calificaciones/', mostrar_calificaciones, name='calificaciones'),
    
]