from django.db import models

# Create your models here.
class TipoEmpleado(models.Model):
    tipo = models.CharField(max_length=40)
    
    def __str__(self):
	    return self.tipo
    
class Empleado(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    nacimiento = models.DateField()
    foto = models.ImageField(blank=True, null=True)
    
    def __str__(self):
	    return self.rut
    
    
