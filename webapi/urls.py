from django.urls import re_path
from webapi.autor.views import autor_detail, autor_list
from webapi.editorial.views import editorial_list
from webapi.genero.views import genero_list
from webapi.idioma.views import idioma_list
from webapi.libro.views import libro_list, libro_detail
from webapi.estudiante.views import estudiante_list, estudiante_detail
from django.http import JsonResponse 
urlpatterns = [

    #Genero
 
    #Autor
    re_path(r'^api/autores$', autor_list),
    re_path(r'^api/autores/(?P<id>\d+)$', autor_detail),
    re_path(r'^api/editorial$', editorial_list),
    re_path(r'^api/generos$', genero_list),
    re_path(r'^api/idiomas$', idioma_list),
    re_path(r'^api/libro$', libro_list),
    re_path(r'^api/libro/(?P<id>\d+)$',libro_detail),
    re_path(r'^api/estudiante$', estudiante_list),
    re_path(r'^api/estudiante/(?P<id>\d+)$', estudiante_detail),

]
