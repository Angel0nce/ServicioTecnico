from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField( max_length=255)
    correo = models.EmailField( max_length=255)
    telefono = models.IntegerField()
    direccion = models.CharField( max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre

