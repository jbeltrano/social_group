from django.urls import path
from core.views import Usuario_view, Receta_view, Login_view, Like_view

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
    # URLs de likes
    path('<int:receta_id>/like/', Like_view.toggle_like, name='toggle_like'),
]
