import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.controllers.Controlador_receta import obtener_recetas
from core.controllers.Controlador_receta import obtener_receta
from core.controllers.Controlador_receta import insertar_receta
from core.controllers.Controlador_receta import obtener_recetas_por_usuario
from core.controllers.Controlador_receta import buscar_recetas_usuario, actualizar_receta
from core.controllers.Controlador_receta import obtener_recetas_por_tiempo
from core.controllers.Controlador_receta import buscar_recetas
from core.controllers.Controlador_receta import eliminar_receta
from core.controllers.Controlador_receta import obtener_receta_vacia
from core.controllers.Controlador_categoria import obtener_categorias
from core.controllers.Controlador_receta_categoria import obtener_recetas_por_categoria
from core.controllers.Controlador_receta_categoria import insertar_receta_categoria
from core.controllers.Controlador_receta_categoria import obtener_categorias_de_receta
from core.controllers.Controlador_receta_categoria import eliminar_categorias_de_receta
from core.controllers.Controlador_favorito import eliminar_favorito
from core.controllers.Controlador_favorito import obtener_recetas_favoritas_por_usuario
from core.controllers.Controlador_favorito import insertar_favorito
from core.controllers.Controlador_favorito import es_favorito
from core.controllers.Controlador_like import insertar_like
from core.controllers.Controlador_like import eliminar_like
from core.controllers.Controlador_like import es_like
from core.controllers.Controlador_like import obtener_recetas_like_por_usuario
from core.controllers.Controlador_calificacion import obtener_calificaciones_por_receta
from core.controllers.Controlador_calificacion import obtener_calificacion
from core.controllers.Controlador_calificacion import insertar_calificacion
from core.controllers.Controlador_calificacion import actualizar_calificacion
from core.controllers.Controlador_calificacion import es_calificacion
from .Login_view import login_requerido


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
    es_like_flag = False
    calificacion_usuario = None

    if usuario_correo:
        es_favorito_flag = es_favorito(usuario_correo, receta_id)
        es_like_flag = es_like(usuario_correo, receta_id)

    if es_calificacion(receta_id, usuario_correo):
        calificacion_usuario = obtener_calificacion(receta_id, usuario_correo)


    # ✅ Obtener comentarios desde tu controlador
    comentarios = obtener_calificaciones_por_receta(receta_id)

    context = {
        'receta': receta,
        'comentarios': comentarios,
        'es_favorito': es_favorito_flag,
        'es_like': es_like_flag,
        'usuario_correo': usuario_correo,  # puede ser None si no hay sesión
        'calificacion_usuario': calificacion_usuario
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

        receta = obtener_receta_vacia()

        receta.nombre = request.POST.get("nombre")
        imagen_receta = request.FILES.get("imagen")
        receta.descripcion = request.POST.get("descripcion")
        receta.ingredientes = request.POST.get("lista_ingredientes", "")
        receta.pasos = request.POST.get("pasos", "")
        horas = request.POST.get("horas", 0)
        minutos = request.POST.get("minutos", 0)
        receta.porcion = request.POST.get("porcion", 1)
        usuario_correo = request.session.get("usuario_id")
        categorias_ids = request.POST.getlist("categorias")  # puede devolver varias

        # Guardamos la receta
        receta = insertar_receta(
            receta,
            imagen_file=imagen_receta,
            hora=horas,
            minuto=minutos,
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
        receta.nombre = request.POST.get("nombre",receta.nombre)
        receta.descripcion = request.POST.get("descripcion",receta.descripcion)
        receta.ingredientes = request.POST.get("lista_ingredientes", receta.ingredientes)
        receta.pasos = request.POST.get("pasos", receta.pasos)
        hora = request.POST.get("horas", 0)
        minuto = request.POST.get("minutos", 0)
        receta.porcion = request.POST.get("porcion", receta.porcion)

        # Imagen: si se sube una nueva, reemplaza la anterior
        nueva_imagen = request.FILES.get("imagen")
        if nueva_imagen:
            receta.imagen = nueva_imagen

        # Actualizar la receta
        actualizar_receta(receta,imagen_file=nueva_imagen,hora=hora,minuto=minuto,)

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

    recetas = obtener_recetas_favoritas_por_usuario(usuario_id)

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


@login_requerido
def recetas_like_view(request):

    usuario_id = request.session.get('usuario_id')
    page = request.GET.get('page', 1)

    recetas = obtener_recetas_like_por_usuario(usuario_id)
    # Configurar la paginación
    paginator = Paginator(recetas, 45)  # 45 recetas por página
    recetas_pagina = paginator.get_page(page)

    context = {
        'recetas': recetas_pagina,
    }
    return render(request, 'recetas/recetas_like.html', context)


@csrf_exempt
@login_requerido
def eliminar_like_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receta_id = data.get("receta_id")
        usuario_correo = request.session.get("usuario_id")
        eliminar_like(usuario_correo, receta_id)
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def insertar_like_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        receta_id = data.get("receta_id")
        usuario_correo = request.session.get("usuario_id")
        if not usuario_correo:
            return JsonResponse({"error": "Usuario no autenticado"}, status=401)

        if es_like(usuario_correo, receta_id):
            eliminar_like(usuario_correo, receta_id)
        else:
            insertar_like(usuario_correo, receta_id)

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Método no permitido"}, status=405)

def insertar_comentario_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usuario_correo = request.session.get("usuario_id")
        receta_id = data.get("receta_id")
        texto = data.get("texto")
        calificacion = int(data.get("calificacion"))

        if not es_calificacion(receta_id, usuario_correo):
            insertar_calificacion(receta_id, usuario_correo, calificacion, comentario=texto)
        else:
            actualizar_calificacion(
                receta_id,
                usuario_correo,
                puntaje=calificacion,
                comentario=texto
            )
        return JsonResponse({"success": True})

    return JsonResponse({"error": "Método no permitido"}, status=405)
