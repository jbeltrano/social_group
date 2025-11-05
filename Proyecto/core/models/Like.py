from django.db import models
from .Usuario import Usuario  # importa el modelo usuario
from .Receta import Receta  # importa el modelo receta

class Like(models.Model):
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

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'like'
        unique_together = (('receta', 'usuario'),)