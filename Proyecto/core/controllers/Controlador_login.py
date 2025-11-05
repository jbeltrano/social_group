from .Controlador_usuario import obtener_usuario
from .Controlador_validaciones import validar_correo, validar_contraseña, validar_obligatoriedad, validar_longitud_contraseña
from core.models.Usuario import Usuario

def verificar_login(correo, contraseña):
    error = None
    try:
        usuario = obtener_usuario(correo=correo)
        if not validar_contraseña(contraseña,usuario.contraseña):
            error = "Contraseña incorrecta"
    except Usuario.DoesNotExist:
        error = "Usuario no encontrado"
    return error
    
  
def verificar_registro(nombre, apellido, correo, contraseña, contraseña_confirmada):
    errores = []

    if not validar_obligatoriedad([nombre, apellido, correo, contraseña, contraseña_confirmada]):
        errores.append("Todos los campos son obligatorios.")

    if not validar_correo(correo):
        errores.append("El correo electrónico no es válido.")

    if contraseña != contraseña_confirmada:
        errores.append("Las contraseñas no coinciden.")

    if not validar_longitud_contraseña(contraseña):
        errores.append("La contraseña debe tener al menos 8 caracteres.")

    return (errores)

def iniciar_sesion(request, usuario):
    request.session["usuario_id"] = usuario.correo
    request.session["usuario_nombre"] = usuario.nombre