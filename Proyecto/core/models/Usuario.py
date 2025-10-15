from django.db import models

class Usuario(models.Model):
    correo = models.EmailField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    password = models.CharField(max_length=255, db_column='contrasena')

    class Meta:
        managed = False      # si la tabla ya existe
        db_table = 'usuario'
