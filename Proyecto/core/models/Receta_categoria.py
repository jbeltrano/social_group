from django.db import models
from .Categoria import Categoria
from .Receta import Receta

class Receta_categoria(models.Model):
    id = models.ForeignKey(
        'Receta',
        db_column='id',             # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )
    cat_id = models.ForeignKey(
        'Categoria',
        db_column='cat_id',           # columna real en la base de datos
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False     # Django no la recreará
        db_table = 'receta_categoria'
        unique_together = (('id', 'cat_id'),)