from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import datetime

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    mensaje = "Artículo buscado: %r" % request.GET["prd"]
    return HttpResponse(mensaje)
