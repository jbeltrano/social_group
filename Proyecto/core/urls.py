from django.urls import path
from core.views import Usuario_view, Receta_view, Login_view
from django.views.generic import RedirectView
from django.urls import path

urlpatterns = [
    # URLs de autenticación
    path('login/', Login_view.login_view, name='login'),
    path('logout/', Login_view.logout_view, name='logout'),
    path('registro/', Login_view.registro_view, name='registro'),
    # URLs de usuarios
    path('usuarios/', Usuario_view.lista_usuarios_view, name='lista_usuarios'),
    
    # URLs de recetas
    path('', Receta_view.lista_recetas, name='lista_recetas'),
    path('<int:receta_id>/', Receta_view.detalle_receta, name='detalle_receta'),
    path('<int:receta_id>/imagen/', Receta_view.obtener_imagen_receta, name='obtener_imagen_receta'),
    path('nueva/', Receta_view.formulario_receta, name='formulario_receta'),
    path('mis_recetas/', Receta_view.mis_recetas_view, name='mis_recetas'),

    path('favicon.ico', RedirectView.as_view(url='/static/core/favicon.ico')),
]
