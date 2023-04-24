from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from webapi.models import Libro
from webapi.serializers import LibroSerializer


@api_view(['GET', 'POST'])
def libro_list(request):
    if request.method == 'GET':
        # Lógica para obtener todos los libros
        libros = Libro.objects.all()
        # Serializar los datos
        serializer = LibroSerializer(libros, many=True)
        # Retornar los datos serializados en una respuesta JSON
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # Serializar los datos del request
        serializer = LibroSerializer(data=request.data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            # Extraer la imagen del request.data y asignarla al campo 'imagen'
            imagen = request.FILES.get('imagen')
            serializer.validated_data['imagen'] = imagen
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return JsonResponse(serializer.data, status=201)
        # Si los datos no son válidos, retornar una respuesta con error
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def libro_detail(request, id):
    try:
            # Obtener el libro por su ID
        libro = Libro.objects.get(id=id)
    except ObjectDoesNotExist:
        # Si el libro no existe, retornar una respuesta con error
        return JsonResponse({'error': 'Libro no encontrado'}, status=404)

    if request.method == 'GET':
        # Serializar los datos del libro
        serializer = LibroSerializer(libro)
        # Retornar los datos serializados en una respuesta JSON
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)
        # Obtener la imagen del request
        imagen = request.FILES.get('imagen')
        # Agregar la imagen al diccionario de datos
        data['imagen'] = imagen
        # Serializar los datos del libro con los datos del request
        serializer = LibroSerializer(libro, data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return JsonResponse(serializer.data)
        # Si los datos no son válidos, retornar una respuesta con error
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        # Eliminar el libro
        libro.delete()
        # Retornar una respuesta con éxito
        return JsonResponse({'mensaje': 'Libro eliminado con éxito'})
