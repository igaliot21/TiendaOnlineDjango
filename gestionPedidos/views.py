from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.models import Articulos
from gestionPedidos.forms import FormularioContacto
import datetime

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    if request.GET["prd"]:
        #mensaje = "Artículo buscado: %r" % request.GET["prd"]
        productoBuscar = request.GET["prd"]
        if len(productoBuscar) > 30:
            mensaje = "Texto de busqueda demasiado largo"
        else:
            articulos = Articulos.objects.filter(
                nombre__icontains=productoBuscar)
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query": productoBuscar})
    else:
        mensaje = "Busqueda vacia"

    return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":
        subject = request.POST["asunto"] + " " + request.POST["email"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            "josem.izquierdo.galiot@gmail.com", "igaliot21@gmail.com"]
        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)

        return render(request, "gracias.html")

    return render(request, "contacto.html")


def contactoforms(request):
    if request.method == "POST":
        miFormulario = FormularioContacto(request.POST)
        if miFormulario.is_valid():
            dataForm = miFormulario.cleaned_data
            subject = dataForm["asunto"] + " " + dataForm["email"]
            message = dataForm["mensaje"] + " " + dataForm["email"]
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["josem.izquierdo.galiot@gmail.com"]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=False)
            return render(request, "gracias.html")
    else:
        miFormulario = FormularioContacto()

    return render(request, "contactoforms.html", {"form": miFormulario})
