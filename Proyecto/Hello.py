import os
import django

# Establecer el módulo de configuración
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CookShare.settings")

# Inicializar Django
django.setup()

# Ahora puedes usar los modelos
from core.controllers import Controlador_usuario

# Ejemplo de consulta
usuarios = Controlador_usuario.obtener_todos_usuarios()
Controlador_usuario.crear_usuario("juan@gmail.com", "Juan Beltran", "jun1234")
for u in usuarios:
    print(u.nombre, u.correo, u.password)
    print("-----")
