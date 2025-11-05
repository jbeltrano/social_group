from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from core.controllers.Controlador_receta import obtener_recetas, obtener_receta, insertar_receta, obtener_recetas_por_usuario, buscar_recetas_usuario, actualizar_receta
from core.controllers.Controlador_receta import obtener_recetas_por_tiempo, buscar_recetas, eliminar_receta
from core.controllers.Controlador_categoria import obtener_categorias
from core.controllers.Controlador_receta_categoria import obtener_recetas_por_categoria, insertar_receta_categoria, obtener_categorias_de_receta, eliminar_categorias_de_receta
from core.controllers.Controlador_favorito import eliminar_favorito, obtener_recetas_favoritas_por_usuario as recetas_favoritas_usuario, insertar_favorito, es_favorito
from core.views.Login_view import login_requerido
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

    usuario_correo = request.session.get("usuario_id")
    es_favorito_flag = False

    if usuario_correo:
        try:
            es_favorito_flag = es_favorito(usuario_correo, receta_id)
        except Exception as e:
            print("Error verificando favorito:", e)

    context = {
        'receta': receta,
        'es_favorito': es_favorito_flag,
        'usuario_correo': usuario_correo  # puede ser None si no hay sesión
    }
    return render(request, 'recetas/detalle_receta.html', context)


def obtener_imagen_receta(request, receta_id):
    receta = obtener_receta(receta_id)
    if receta and receta.imagen:
        return HttpResponse(receta.imagen, content_type='image/jpeg')
    return HttpResponse(status=404)


@login_requerido
def formulario_receta(request):
    if request.method == 'POST':

        nombre_receta = request.POST.get("nombre")
        imagen_receta = request.FILES.get("imagen")
        descripcion = request.POST.get("descripcion")
        ingredientes = request.POST.get("lista_ingredientes", "")
        pasos = request.POST.get("pasos", "")
        horas = request.POST.get("horas", 0)
        minutos = request.POST.get("minutos", 0)
        porcion = request.POST.get("porcion", 1)
        usuario_correo = request.session.get("usuario_id")
        categorias_ids = request.POST.getlist("categorias")  # puede devolver varias

        # Guardamos la receta
        receta = insertar_receta(
            nombre=nombre_receta,
            imagen_file=imagen_receta,
            descripcion=descripcion,
            ingredientes=ingredientes,
            pasos=pasos,
            hora=horas,
            minuto=minutos,
            porcion=porcion,
            usuario_correo=usuario_correo
        )

        if receta and categorias_ids:
            for categoria in categorias_ids:
                insertar_receta_categoria(receta.id, categoria)

        return redirect('lista_recetas')
    
    # Se obtienen las categorías desde la base de datos
    categorias = obtener_categorias()
    context = {
        'categorias': categorias
    }
    return render(request, 'recetas/formulario_receta.html', context)


@login_requerido
def mis_recetas_view(request):

    usuario_id = request.session.get('usuario_id')
    
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    filtro_hora = request.GET.get('horas', '')
    filtro_minuto = request.GET.get('minutos', '')
    page = request.GET.get('page', 1)
    
    # Obtener todas las categorías para el dropdown
    categorias = obtener_categorias()
    
    # Obtener las recetas según la categoría seleccionada
    if categoria_id and categoria_id.isdigit():
        recetas = obtener_recetas_por_categoria(int(categoria_id), usuario_id)
    else:
        recetas = obtener_recetas_por_usuario(usuario_id)
        
    recetas = obtener_recetas_por_tiempo(recetas, filtro_hora, filtro_minuto, usuario_id)

    # Aplicar filtro si hay término de búsqueda
    recetas = buscar_recetas_usuario(recetas, query, usuario_id)
    
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
    return render(request, 'recetas/mis_recetas.html', context)

@login_requerido
def editar_receta_view(request, receta_id):

    receta = obtener_receta(receta_id)

    if not receta or receta.usuario.correo != request.session.get("usuario_id"):
        return redirect('mis_recetas')
    
    if request.method == 'POST':
        nombre = request.POST.get("nombre",receta.nombre)
        descripcion = request.POST.get("descripcion",receta.descripcion)
        ingredientes = request.POST.get("lista_ingredientes", receta.ingredientes)
        pasos = request.POST.get("pasos", receta.pasos)
        hora = request.POST.get("horas", 0)
        minuto = request.POST.get("minutos", 0)
        porcion = request.POST.get("porcion", receta.porcion)

        # Imagen: si se sube una nueva, reemplaza la anterior
        nueva_imagen = request.FILES.get("imagen")
        if nueva_imagen:
            receta.imagen = nueva_imagen

        # Actualizar la receta
        actualizar_receta(
            receta,
            nombre=nombre,
            imagen_file=nueva_imagen,
            descripcion=descripcion,
            ingredientes=ingredientes,
            pasos=pasos,
            hora=hora,
            minuto=minuto,
            porcion=porcion
        )

        # Actualizar categorías
        categorias_ids = request.POST.getlist("categorias")
        eliminar_categorias_de_receta(receta_id)
        if categorias_ids:
            for categoria_id in categorias_ids:
                insertar_receta_categoria(receta.id, categoria_id)

        return redirect('mis_recetas')

    # Método GET → mostrar formulario con datos actuales
    categorias = obtener_categorias()
    categorias_receta = obtener_categorias_de_receta(receta_id)
    

    context = {
        'receta': receta,
        'categorias': categorias,
        'categorias_receta': list(categorias_receta)
    }

    return render(request, 'recetas/editar_receta.html', context)

@require_POST
@login_requerido
def eliminar_receta_view(request, receta_id):
    receta = obtener_receta(receta_id)

    if not receta or receta.usuario.correo != request.session.get("usuario_id"):
        return redirect('lista_recetas')

    eliminar_receta(receta_id)
    return redirect('mis_recetas')

@login_requerido
def recetas_favoritas_view(request):

    usuario_id = request.session.get('usuario_id')
    page = request.GET.get('page', 1)
    
    recetas = recetas_favoritas_usuario(usuario_id)
    
    # Configurar la paginación
    paginator = Paginator(recetas, 45)  # 45 recetas por página
    recetas_pagina = paginator.get_page(page)
    
    context = {
        'recetas': recetas_pagina,
    }
    return render(request, 'recetas/recetas_favoritas.html', context)



@csrf_exempt
@login_requerido
def eliminar_favorito_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receta_id = data.get("receta_id")
        usuario_correo = request.session.get("usuario_id")
        eliminar_favorito(usuario_correo, receta_id)
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def insertar_favorito_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receta_id = data.get("receta_id")
        usuario_correo = request.session.get("usuario_id")
        if not usuario_correo:
            return JsonResponse({"error": "Usuario no autenticado"}, status=401)

        if es_favorito(usuario_correo, receta_id):
            eliminar_favorito(usuario_correo, receta_id)
        else:
            insertar_favorito(usuario_correo, receta_id)

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Método no permitido"}, status=405)