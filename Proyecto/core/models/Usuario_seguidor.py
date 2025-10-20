from django.db import models
from .Usuario import Usuario  # importa el modelo usuario

class Usuario_seguidor(models.Model):
    usuario_seguidor = models.ForeignKey(
        'Usuario',
        db_column='usuario_seguidor',             # columna real en la base de datos
        on_delete=models.CASCADE,
    )

    usuario_seguido = models.ForeignKey(
        'Usuario',
        db_column='usuario_seguido',             # columna real en la base de datos
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'usuario_seguidor'
        unique_together = (('usuario_seguidor', 'usuario_seguido'),)