import os
import django

# Establecer el módulo de configuración
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CookShare.settings")

# Inicializar Django
django.setup()

# Ahora puedes usar los modelos
from core.models.Usuario import Usuario
from core.models.Receta import Receta

# Ejemplo de consulta
usuarios = Usuario.objects.all()

for u in usuarios:
    print(u.nombre, u.correo)
