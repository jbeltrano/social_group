import pytest
from core.controllers.Controlador_usuario import insertar_usuario, usuario_existe

@pytest.mark.django_db
def test_usuario_existe_true():
    insertar_usuario("correo@test.com", "Juan", "12345678")
    assert usuario_existe("correo@test.com") is True

@pytest.mark.django_db
def test_usuario_existe_false():
    assert usuario_existe("noexiste@test.com") is False

@pytest.mark.django_db
def test_usuario_existe_borde():
    assert usuario_existe("") is False
    assert usuario_existe("   ") is False