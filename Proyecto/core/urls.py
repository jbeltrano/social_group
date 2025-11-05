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
    path('mis_recetas/editar/<int:receta_id>/', Receta_view.editar_receta_view, name='editar_receta'),
    path('mis_recetas/eliminar/<int:receta_id>/', Receta_view.eliminar_receta_view, name='eliminar_receta'),
    path('recetas_favoritas/', Receta_view.recetas_favoritas_view, name='recetas_favoritas'),
    path('recetas_favoritas/eliminar/<int:receta_id>/', Receta_view.eliminar_favorito_view, name='eliminar_receta_favorita'),
    path('recetas_favoritas/eliminar/', Receta_view.eliminar_favorito_view, name='eliminar_favorito'),
    path('recetas_favoritas/insertar/', Receta_view.insertar_favorito_view, name='insertar_favorito'),
    path('recetas_like/', Receta_view.recetas_like_view, name='recetas_like'),
    path('recetas_like/eliminar/', Receta_view.eliminar_like_view, name='eliminar_like'),
    path('recetas_like/insertar/', Receta_view.insertar_like_view, name='insertar_like'),

    path('favicon.ico', RedirectView.as_view(url='/static/core/favicon.ico')),
]
