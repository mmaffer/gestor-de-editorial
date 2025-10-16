# catalog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EditorialViewSet, LibroViewSet

# El router se encarga de generar las URLs para nuestros ViewSets
router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')       # /api/libros/
router.register(r'editoriales', EditorialViewSet, basename='editorial') # /api/editoriales/

urlpatterns = [
    path('', include(router.urls)),
]