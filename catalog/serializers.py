# catalog/serializers.py

from rest_framework import serializers
from .models import Editorial, Libro

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    # ✨ Punto Extra: Personalizamos la respuesta para mostrar el nombre
    # de la editorial, no solo su ID.
    editorial_nombre = serializers.CharField(source='editorial.nombre', read_only=True)

    class Meta:
        model = Libro
        # 'editorial' es para escribir (enviar el ID), 'editorial_nombre' es para leer.
        fields = ['id', 'titulo', 'genero', 'año', 'editorial', 'editorial_nombre']