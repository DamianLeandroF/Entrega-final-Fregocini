from django.db import models

# Create your models here.






class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"

class Tutor(models.Model):
    nombre = models.CharField(max_length=20)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    numero_camada = models.IntegerField()
