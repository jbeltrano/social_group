import os
import django

# Establecer el módulo de configuración
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CookShare.settings")

# Inicializar Django
django.setup()

# Ahora puedes usar los modelos
from core.controllers import Controlador_usuario, Controlador_receta

# Función para leer la imagen como bytes
def leer_imagen(ruta_imagen):
    with open(ruta_imagen, 'rb') as img_file:
        return img_file.read()

# Ejemplo de consulta
# Asegúrate de que la ruta de la imagen sea correcta
ruta_imagen = r"c:\Users\juanp\Downloads\Carbonara-editada.jpg"  # Usando raw string con 'r' prefix
imagen_bytes = leer_imagen(ruta_imagen)


usuarios = Controlador_usuario.obtener_todos_usuarios()
recetas = Controlador_receta.obtener_recetas()
for u in usuarios:
    print(u.nombre, u.correo, u.contraseña)
    print("-----")


for r in recetas:
    print(r.nombre, r.descripcion, r.ingredientes, r.pasos)
    print("-----")