from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile  # Paso 1
from webapi.models import Estudiante
from webapi.serializers import EstudianteSerializer

@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        # Lógica para obtener todos los estudiantes
        estudiantes = Estudiante.objects.all()
        # Serializar los datos
        serializer = EstudianteSerializer(estudiantes, many=True)
        # Retornar los datos serializados en una respuesta JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)

        # Obtener la imagen del request
        imagen = request.FILES.get('imagen')

        # Crear un archivo en memoria a partir de la imagen recibida en el request
        imagen_archivo = SimpleUploadedFile(imagen.name, imagen.read())  # Paso 2

        # Agregar la ruta de la imagen al diccionario de datos
        data['imagen'] = imagen_archivo

        # Serializar los datos
        serializer = EstudianteSerializer(data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si los datos no son válidos, retornar una respuesta con error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detail(request, id):
    try:
        # Obtener el estudiante por su ID
        estudiante = Estudiante.objects.get(id=id)
    except ObjectDoesNotExist:
        # Si el estudiante no existe, retornar una respuesta con error
        return Response({'error': 'Estudiante no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serializar los datos del estudiante
        serializer = EstudianteSerializer(estudiante)
        # Retornar los datos serializados en una respuesta JSON
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)

        # Obtener la imagen del request
        imagen = request.FILES.get('imagen')

        # Crear un archivo en memoria a partir de la imagen recibida en el request
        imagen_archivo = SimpleUploadedFile(imagen.name, imagen.read())  # Paso 2

        # Agregar la ruta de la imagen al diccionario de datos
        data['imagen'] = imagen_archivo
        # Serializar los datos del estudiante con los datos del request
        serializer = EstudianteSerializer(estudiante, data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos actualizados
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Si los datos no son válidos, retornar una respuesta con error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Eliminar el estudiante
        estudiante.delete()
        # Retornar una respuesta con mensaje de éxito
        return Response({'message': 'Estudiante eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
