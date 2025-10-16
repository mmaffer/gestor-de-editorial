# catalog/views.py

from rest_framework import viewsets, filters
from .models import Editorial, Libro
from .serializers import EditorialSerializer, LibroSerializer

# 📚 CRUD básico de Entidad 2 (Editorial)
class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

# 📃 Listado, ➕ Creación, ✏️ Edición, ❌ Eliminación y 🔍 Búsqueda de Entidad 1 (Libro)
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    
    # 🔍 Implementación de búsqueda por filtros
    filter_backends = [filters.SearchFilter]
    # Campos por los que el cliente podrá buscar
    search_fields = ['titulo', 'genero']