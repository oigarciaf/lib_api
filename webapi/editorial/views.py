from django.shortcuts import render

from django.db import models
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from webapi.models import Editorial
from webapi.serializers import EditorialSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse 

@api_view(['GET', 'POST'])
def editorial_list(request):
    if request.method == 'GET':
        # Lógica para obtener todas las editoriales
        editoriales = Editorial.objects.all()
        # Serializar los datos
        serializer = EditorialSerializer(editoriales, many=True)
        # Retornar los datos serializados en una respuesta JSON
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)
        # Serializar los datos
        serializer = EditorialSerializer(data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return JsonResponse(serializer.data, status=201)
        # Si los datos no son válidos, retornar una respuesta con error
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def editorial_detail(request, id):
    try:
        editorial = Editorial.objects.get(id=id)
    except Editorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EditorialSerializer(editorial)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = EditorialSerializer(editorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        editorial.delete()
        return JsonResponse({'message': 'Editorial eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
