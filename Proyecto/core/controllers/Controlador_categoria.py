from core.models.Categoria import Categoria

def obtener_categorias():
    return Categoria.objects.all().order_by('nombre')

def obtener_categoria(id):
    return Categoria.objects.filter(id=id).first()