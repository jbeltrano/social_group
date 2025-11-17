import pytest
from django.contrib.auth.hashers import check_password
from core.controllers.Controlador_usuario import insertar_usuario
from core.models.Usuario import Usuario

@pytest.mark.django_db
def test_insertar_usuario_valido():
    usuario = insertar_usuario("prueba@test.com", "   juan perez   ", "12345678")

    assert usuario.correo == "prueba@test.com"
    assert usuario.nombre == "Juan Perez"  # strip() + title()
    assert check_password("12345678", usuario.contraseña)

@pytest.mark.django_db
def test_insertar_usuario_nombre_formateado():
    usuario = insertar_usuario("otro@test.com", "    maria   lopez ", "password")
    assert usuario.nombre == "Maria Lopez"

@pytest.mark.django_db
def test_insertar_usuario_contrasena_vacia():
    usuario = insertar_usuario("vacio@test.com", "Nombre", "")
    # Contraseña vacía también se encripta usando make_password("")
    assert check_password("", usuario.contraseña)