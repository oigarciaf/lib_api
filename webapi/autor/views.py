from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from webapi.models import Autor
from webapi.serializers import AutorSerializer


@api_view(['GET', 'POST'])
def autor_list(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guardar los datos en la base de datos
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def autor_detail(request, id):
    try:
        autor = Autor.objects.get(id=id)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        autor.delete()
        return JsonResponse({'message': 'Autor eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)
