import os
import django

# Establecer el módulo de configuración
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CookShare.settings")

# Inicializar Django
django.setup()

# Ahora puedes usar los modelos
from Proyecto.core.controllers import Controlador_usuario

# Ejemplo de consulta
usuarios = Controlador_usuario.obtener_todos_usuarios()

for u in usuarios:
    print(u.nombre, u.correo, u.password)
    print("-----")
