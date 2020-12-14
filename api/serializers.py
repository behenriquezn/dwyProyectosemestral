from rest_framework import serializers
from core.models import Producto,Tienda

# creando la clase que permite serializar el modelo

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [ "numeroIdentificador", "nombre", "valor", "valorpresupuestado","notas","tiendanombre"]


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ("nombre","nombresucursal","direccion","ciudad","region")
