from django.db import models
from .Usuario import Usuario  # importa el modelo usuario

class Usuario_seguidor(models.Model):
    seguidor = models.ForeignKey(
        'Usuario',
        db_column='seguidor',             # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )

    seguido = models.ForeignKey(
        'Usuario',
        db_column='seguido',             # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'usuario_seguidor'
        unique_together = (('seguidor', 'seguido'),)