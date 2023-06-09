from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from webapi.models import GeneroLibro
from webapi.serializers import GeneroLibroSerializer

@api_view(['GET', 'POST'])
def genero_list(request):
    if request.method == 'GET':
        # Lógica para obtener todos los géneros de libros
        generos_libro = GeneroLibro.objects.all()
        # Serializar los datos
        serializer = GeneroLibroSerializer(generos_libro, many=True)
        # Retornar los datos serializados en una respuesta JSON
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)
        # Serializar los datos
        serializer = GeneroLibroSerializer(data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return JsonResponse(serializer.data, status=201)
        # Si los datos no son válidos, retornar una respuesta con error
        return JsonResponse(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def genero_detail(request, id):
    try:
        genero = GeneroLibro.objects.get(id=id)
    except GeneroLibro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GeneroLibroSerializer(genero)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = GeneroLibroSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        genero.delete()
        return JsonResponse({'message': 'GeneroLibro eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
