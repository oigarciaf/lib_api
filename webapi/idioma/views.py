from django.db import models
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist
from webapi.models import Idioma
from webapi.serializers import IdiomaSerializer

@api_view(['GET', 'POST'])
def idioma_list(request):
    if request.method == 'GET':
        # Lógica para obtener todos los idiomas
        idiomas = Idioma.objects.all()
        # Serializar los datos
        serializer = IdiomaSerializer(idiomas, many=True)
        # Retornar los datos serializados en una respuesta JSON
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # Parsear los datos del request en un diccionario
        data = JSONParser().parse(request)
        # Serializar los datos
        serializer = IdiomaSerializer(data=data)
        # Validar y guardar los datos si son válidos
        if serializer.is_valid():
            serializer.save()
            # Retornar una respuesta JSON con los datos guardados
            return JsonResponse(serializer.data, status=201)
        # Si los datos no son válidos, retornar una respuesta con error
        return JsonResponse(serializer.errors, status=400)