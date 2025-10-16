# catalog/models.py

from django.db import models

# Entidad 2: Editorial
class Editorial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Entidad 1: Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    año = models.IntegerField()
    # 📌 Relación: Un libro pertenece a una editorial
    editorial = models.ForeignKey(Editorial, related_name='libros', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo