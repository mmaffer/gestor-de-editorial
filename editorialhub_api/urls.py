# editorialhub_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conecta las URLs de nuestra app bajo el prefijo 'api/'
    path('api/', include('catalog.urls')),
]