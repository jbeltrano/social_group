from django.db import models
from .Usuario import Usuario  # importa el modelo usuario
from .Receta import Receta  # importa el modelo receta

class Calificacion(models.Model):
    receta = models.ForeignKey(
        'Receta',
        db_column='receta_id',                 # columna real en la base de datos
        on_delete=models.CASCADE,
    )
    usuario = models.ForeignKey(
        'Usuario',
        db_column='usuario_correo',             # columna real en la base de datos
        on_delete=models.CASCADE,
    )
    puntaje = models.SmallIntegerField(db_column='numero')
    comentario = models.TextField(null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'calificacion'
        unique_together = (('receta_id', 'usuario_correo'),)