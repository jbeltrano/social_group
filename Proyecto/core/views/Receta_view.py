from django.shortcuts import render
from django.http import HttpResponse
from core.controllers.Controlador_receta import obtener_recetas, obtener_receta
from django.db.models import Q

def lista_recetas(request):
    # Obtener el término de búsqueda
    query = request.GET.get('q', '')
    
    # Obtener todas las recetas
    recetas = obtener_recetas()
    
    # Aplicar filtro si hay término de búsqueda
    if query:
        recetas = recetas.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(ingredientes__icontains=query)
        )
    
    context = {
        'recetas': recetas,
        'query': query
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
