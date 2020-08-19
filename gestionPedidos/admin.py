from django.contrib import admin
from gestionPedidos.models import Cliente, Articulos, Pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email", "telefono")
    search_fields = ("nombre", "telefono")


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    search_fields = ("nombre", "seccion", "precio")
    list_filter = ("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    search_fields = ("numero", "fecha", "entregado")
    list_filter = ("entregado", "fecha")
    date_hierarchy = "fecha"


admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
