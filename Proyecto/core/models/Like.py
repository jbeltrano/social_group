from django.db import models
from .Usuario import Usuario  # importa el modelo usuario
from .Receta import Receta  # importa el modelo receta

class Like(models.Model):
    id = models.ForeignKey(
        'Receta',
        db_column='id',                 # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )
    correo = models.ForeignKey(
        'Usuario',
        db_column='correo',             # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'like'
        unique_together = (('id', 'correo'),)