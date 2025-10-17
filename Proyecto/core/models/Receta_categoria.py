from django.db import models
from .Categoria import Categoria
from .Receta import Receta

class Receta_categoria(models.Model):
    receta_id = models.ForeignKey(
        'Receta',
        db_column='receta_id',             # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )
    categoria_id = models.ForeignKey(
        'Categoria',
        db_column='categoria_id',           # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'receta_categoria'
        unique_together = (('receta_id', 'categoria_id'),)