from django.shortcuts import render

from core.models import Insumo, ContactoFinal
from .serializers import InsumoSerializer,ContactoFinalSerializer
from rest_framework import generics
# Create your views here.

class InsumoViewSet(generics.ListCreateAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

class InsumoFiltroNombreViewSet(generics.ListAPIView):
    serializer_class = InsumoSerializer
    #utilizar el metodo get_queryset 
    def get_queryset(self):
        #se necesita recuperar un parametro desde la url 
        elnombre = self.kwargs['nombre']
        return Insumo.objects.filter(nombre=elnombre)

class InsumoFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = InsumoSerializer
    #utilizar el metodo get_queryset 
    def get_queryset(self):
        #se necesita recuperar un parametro desde la url 
        elprecio = self.kwargs['precio']
        return Insumo.objects.filter(precio=elprecio)

class ContactoFinalViewSet(generics.ListCreateAPIView):
    queryset = ContactoFinal.objects.all()
    serializer_class = ContactoFinalSerializer
