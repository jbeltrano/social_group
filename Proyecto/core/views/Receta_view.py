from django.shortcuts import render
from django.http import HttpResponse
from core.controllers.Controlador_receta import obtener_recetas, obtener_receta, obtener_recetas_por_tiempo, buscar_recetas
from core.controllers.Controlador_like import tiene_like, contar_likes
from core.controllers.Controlador_categoria import obtener_categorias
from core.controllers.Controlador_receta_categoria import obtener_recetas_por_categoria
from django.core.paginator import Paginator


def lista_recetas(request):
    # Obtener el término de búsqueda, la categoría y el tiempo seleccionado
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    filtro_hora = request.GET.get('horas', '')
    filtro_minuto = request.GET.get('minutos', '')
    page = request.GET.get('page', 1)
    
    # Obtener todas las categorías para el dropdown
    categorias = obtener_categorias()
    
    # Obtener las recetas según la categoría seleccionada
    if categoria_id and categoria_id.isdigit():
        recetas = obtener_recetas_por_categoria(int(categoria_id))
    else:
        recetas = obtener_recetas()
        
    recetas = obtener_recetas_por_tiempo(recetas, filtro_hora, filtro_minuto)

    # Aplicar filtro si hay término de búsqueda
    recetas = buscar_recetas(recetas, query)
    
    # Configurar la paginación
    paginator = Paginator(recetas, 45)  # 45 recetas por página
    recetas_pagina = paginator.get_page(page)
    
    context = {
        'recetas': recetas_pagina,
        'query': query,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id,
        'horas_seleccionadas': filtro_hora,
        'minutos_seleccionados': filtro_minuto
    }
    return render(request, 'recetas/lista_recetas.html', context)


def detalle_receta(request, receta_id):
    receta = obtener_receta(receta_id)
    if not receta:
        return HttpResponse("Receta no encontrada", status=404)
    
    # Obtener información de likes
    usuario_correo = request.session.get("usuario_id")
    user_has_liked = False
    if usuario_correo:
        user_has_liked = tiene_like(receta_id, usuario_correo)
    likes_count = contar_likes(receta_id)
    
    context = {
        'receta': receta,
        'user_has_liked': user_has_liked,
        'likes_count': likes_count
    }
    return render(request, 'recetas/detalle_receta.html', context)


def obtener_imagen_receta(request, receta_id):
    receta = obtener_receta(receta_id)
    if receta and receta.imagen:
        return HttpResponse(receta.imagen, content_type='image/jpeg')
    return HttpResponse(status=404)
