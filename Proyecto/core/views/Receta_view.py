from django.shortcuts import render
from django.http import HttpResponse
from core.controllers.Controlador_receta import obtener_recetas, obtener_receta
from core.controllers.Controlador_categoria import obtener_categorias
from core.controllers.Controlador_receta_categoria import obtener_recetas_por_categoria
from django.db.models import Q


def lista_recetas(request):
    # Obtener el término de búsqueda y la categoría seleccionada
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    # Obtener todas las categorías para el dropdown
    categorias = obtener_categorias()
    
    # Obtener las recetas según la categoría seleccionada
    if categoria_id and categoria_id.isdigit():
        recetas = obtener_recetas_por_categoria(int(categoria_id))
    else:
        recetas = obtener_recetas()
    
    # Aplicar filtro si hay término de búsqueda
    if query:
        recetas = recetas.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(ingredientes__icontains=query) |
            Q(porcion__icontains=query)
        )
    
    context = {
        'recetas': recetas,
        'query': query,
        'categorias': categorias,
        'categoria_seleccionada': categoria_id
    }
    return render(request, 'recetas/lista_recetas.html', context)


def detalle_receta(request, receta_id):
    receta = obtener_receta(receta_id)
    if not receta:
        return HttpResponse("Receta no encontrada", status=404)
    
    context = {
        'receta': receta
    }
    return render(request, 'recetas/detalle_receta.html', context)


def obtener_imagen_receta(request, receta_id):
    receta = obtener_receta(receta_id)
    if receta and receta.imagen:
        return HttpResponse(receta.imagen, content_type='image/jpeg')
    return HttpResponse(status=404)
