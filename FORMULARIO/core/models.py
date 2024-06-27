from django.db import models
from django.contrib.auth.models import User

class Planta(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ProduccionDiaria(models.Model):
    TURNOS = [
        ('AM', 'Mañana'),
        ('PM', 'Tarde'),
        ('MM', 'Noche'),
    ]

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    litros_producidos = models.FloatField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=2, choices=TURNOS)
    hora_registro = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto.nombre} - {self.fecha_produccion} - {self.turno}"
