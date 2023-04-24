from django.db import models

# Create your models here.

# Create your models here.


class Autor(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion
    
class Editorial(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class GeneroLibro(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Idioma(models.Model):
    descripcion  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Libro(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    id_genero_libro = models.ForeignKey(GeneroLibro, on_delete=models.CASCADE)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    edicion = models.IntegerField()
    year_publicacion = models.IntegerField()
    imagen = models.ImageField(upload_to='fotos', null=True)
    resumen = models.TextField()

    def __str__(self):
        return self.titulo + " " + self.id_generolibro + " " + self.id_autor + " " + self.edicion + " " + self.fotolibro

class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identidad = models.CharField(max_length=15)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="fotos", null=True)

    def __str__(self) :
        return self.nombres + "" + self.apellidos + "" + self.identidad + "" + self.telefono + "" + self.imagen
