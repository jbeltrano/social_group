from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False      # si la tabla ya existe
        db_table = 'categoria'
