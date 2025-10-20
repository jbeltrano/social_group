from django.urls import path
from .views import lista_usuarios_view, boton_usuario_view

urlpatterns = [
    path('usuarios/', lista_usuarios_view, name='lista_usuarios'),
    path('', boton_usuario_view, name='boton_usuario'),
]
