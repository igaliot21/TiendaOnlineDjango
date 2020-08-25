from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from gestionPedidos.models import Articulos
import datetime

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Artículo buscado: %r" % request.GET["prd"]
        productoBuscar = request.GET["prd"]
        articulos = Articulos.objects.filter(nombre__icontains=productoBuscar)
        return render(request, "resultado_busqueda.html", {"articulos": articulos, "query": productoBuscar})
    else:
        mensaje = "Busqueda vacia"

    return HttpResponse(mensaje)
