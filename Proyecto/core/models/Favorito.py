from django.db import models
from .Usuario import Usuario
from .Receta import Receta

class Favorito(models.Model):
    receta = models.ForeignKey(
        'Receta',
        db_column='receta_id',
        on_delete=models.CASCADE,
    )
    usuario = models.ForeignKey(
        'Usuario',
        db_column='usuario_correo',
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = False
        db_table = 'favorito'
        unique_together = (('receta', 'usuario'),)
