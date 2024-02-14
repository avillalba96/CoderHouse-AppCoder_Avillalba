from django.urls import path
from .views import agregar_profesor, inicio, agregar_curso, agregar_estudiantes, buscar_cursos

urlpatterns = [
    path('agregar_profesor/', agregar_profesor, name='agregar_profesor'),
    path('inicio/', inicio, name='inicio'),
    path('buscar_cursos/', buscar_cursos, name='buscar_cursos'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    path('agregar_estudiantes/', agregar_estudiantes, name='agregar_estudiantes'),
]
