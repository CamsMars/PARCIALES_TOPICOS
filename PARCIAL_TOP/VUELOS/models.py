from django.db import models

class Vuelo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[('Nacional', 'Nacional'), ('Internacional', 'Internacional')])
    precio = models.FloatField()

    def __str__(self):
        return self.nombre