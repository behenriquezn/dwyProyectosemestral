from django.contrib import admin
from .models import Producto, Tienda

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['numeroIdentificador' ,'nombre','valor','valorpresupuestado','notas','tiendanombre']
    search_fields = ['nombre']
    list_per_page = 10

class TiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombresucursal', 'direccion', 'ciudad', 'region']  
    search_fields = ['nombre']
    list_per_page = 10    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Tienda, TiendaAdmin)
