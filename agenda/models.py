from django.db import models

# Create your models here.

class Agenda(models.Model):
    nombre = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    fecha = models.DateField()
    tipo = models.CharField(max_length=255)