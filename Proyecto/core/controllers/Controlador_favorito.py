from core.models.Favorito import Favorito

def insertar_favorito(usuario, receta):
    favorito = Favorito(usuario=usuario, receta=receta)
    favorito.save()
    return favorito

def eliminar_favorito(usuario, receta):
    return Favorito.objects.filter(usuario=usuario, receta=receta).delete()