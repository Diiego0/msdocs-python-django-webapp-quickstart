# mi_aplicacion/models.py

from django.db import models

class Calificacion(models.Model):
    usuario = models.CharField(max_length=100)
    puntuacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.puntuacion}'
