# codigo generado con IA - ChatGPT

from django.db import models
from .Usuario import Usuario  # importa el modelo usuario

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    creacion = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=255)
    imagen = models.BinaryField(null=True, blank=True)  # Se mapea a MEDIUMBLOB en MySQL
    descripcion = models.TextField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    tiempo = models.TimeField(null=True, blank=True)
    porcion = models.SmallIntegerField(null=True, blank=True)
    calificacion = models.SmallIntegerField(null=True, blank=True)
    verificacion = models.BooleanField(null=True, blank=True)

    # Clave foránea hacia usuario.correo
    usuario = models.ForeignKey(
        Usuario,
        to_field='correo',  # campo en el modelo Usuario
        db_column='usuario_correo',  # nombre de la columna en la tabla receta
        on_delete=models.CASCADE
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'receta'
