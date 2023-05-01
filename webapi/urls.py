from django.urls import re_path
from webapi.autor.views import autor_detail, autor_list
from webapi.editorial.views import editorial_list, editorial_detail
from webapi.genero.views import genero_list, genero_detail
from webapi.idioma.views import idioma_list, idioma_detail
from webapi.libro.views import libro_list, libro_detail
from webapi.estudiante.views import estudiante_list, estudiante_detail
from django.http import JsonResponse 
urlpatterns = [

    #Genero
 
    #Autor
    re_path(r'^api/autores$', autor_list),
    re_path(r'^api/autores/(?P<id>\d+)$', autor_detail),
    re_path(r'^api/editorial$', editorial_list),
    re_path(r'^api/editorial/(?P<id>\d+)$', editorial_detail),
    re_path(r'^api/generos$', genero_list),
    re_path(r'^api/generos/(?P<id>\d+)$', genero_detail),
    re_path(r'^api/idiomas$', idioma_list),
    re_path(r'^api/idiomas/(?P<id>\d+)$', idioma_detail),
    re_path(r'^api/libro$', libro_list),
    re_path(r'^api/libro/(?P<id>\d+)$',libro_detail),
    re_path(r'^api/estudiante$', estudiante_list),
    re_path(r'^api/estudiante/(?P<id>\d+)$', estudiante_detail),

]
