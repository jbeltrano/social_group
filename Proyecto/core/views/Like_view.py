from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models.Receta import Receta
from core.controllers.Controlador_like import dar_like, contar_likes
from core.views.Login_view import login_requerido

@login_requerido
def toggle_like(request, receta_id):
    if request.method == "POST":
        try:
            usuario_correo = request.session.get("usuario_id")
            # Intentar dar/quitar like
            dio_like = dar_like(receta_id, usuario_correo)
            # Obtener el nuevo conteo de likes
            num_likes = contar_likes(receta_id)
            
            return JsonResponse({
                'status': 'success',
                'liked': dio_like,
                'likes_count': num_likes
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)