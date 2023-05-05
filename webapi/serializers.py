from rest_framework import serializers
from .models import Libro, Autor, Editorial, GeneroLibro, Idioma, Estudiante

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('id', 'descripcion')

class GeneroLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLibro
        fields = ('id', 'descripcion')

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = ('id', 'descripcion')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'descripcion', 'id_idioma')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id',
                  'id_autor',
                   'id_editorial',
                   'id_genero_libro',
                   'id_idioma',
                   'codigo',
                   'titulo',
                   'edicion',
                   'year_publicacion',
                   'imagen',
                   'resumen'
                  )
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 
                'nombres',
                'apellidos',
                'identidad',
                'email',
                'telefono',
                'ciudad',
                'imagen'
                )