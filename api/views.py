from django.shortcuts import render

from core.models import Producto , Tienda
from .serializers import ProductosSerializer, TiendaSerializer
from rest_framework import generics
# Create your views here.

class ProductoViewSet(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

class TiendaViewSet(generics.ListCreateAPIView):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer



class ProductoFiltroListaViewSet(generics.ListAPIView):
    serializer_class = ProductosSerializer
    def get_queryset(self):
        nlista = self.kwargs['numeroIdentificador']
        return Producto.objects.filter(numeroIdentificador=nlista)