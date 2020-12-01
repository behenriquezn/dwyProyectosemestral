from rest_framework import serializers
from core.models import Insumo,ContactoFinal


# creando la clase que permite serializar el modelo

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["nombre", "precio", "descripcion","stock"]


class ContactoFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoFinal
        fields = ("nombre","apellido","asunto","tipoCon","mensaje")