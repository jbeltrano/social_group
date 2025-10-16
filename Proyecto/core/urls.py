from django.urls import path
from core.views import Usuario_view

urlpatterns = [
    path('usuarios/', Usuario_view.lista_usuarios_view, name='lista_usuarios'),
    path('', Usuario_view.boton_usuario_view, name='boton_usuario'),
]
