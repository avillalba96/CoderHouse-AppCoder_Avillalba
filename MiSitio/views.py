from django.shortcuts import render, redirect
from .forms import ProfesorForm, CursoForm, EstudiantesForm
from .models import Curso, Profesor, Estudiantes

def inicio(request):
    # Recupera información sobre los cursos para verificar su existencia
    cursos = Curso.objects.all()

    # Pasa la información al contexto
    context = {'cursos': cursos}

    # Renderiza la plantilla con el contexto
    return render(request, 'MiSitio/inicio.html', context)

def buscar_cursos(request):
    numero_camada = request.GET.get('numero_camada', '')
    cursos = Curso.objects.filter(numero_camada__icontains=numero_camada)

    context = {'cursos': cursos, 'numero_camada': numero_camada}
    return render(request, 'MiSitio/buscar_cursos.html', context)

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Verificar si el profesor ya existe por email
            profesor_existente = Profesor.objects.filter(email=email).exists()

            # Si el profesor ya existía, mostrar mensaje de error
            if profesor_existente:
                error_message = "Error: Este email ya existe en la base de datos."
                return render(request, 'MiSitio/agregar_profesor.html', {'form': form, 'error_message': error_message})

            form.save()
            return redirect('agregar_profesor')
    else:
        form = ProfesorForm()

    return render(request, 'MiSitio/agregar_profesor.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            numero_camada = form.cleaned_data['numero_camada']

            # Verificar si el curso ya existe por nombre o número de camada
            curso_existente = Curso.objects.filter(nombre=nombre) | Curso.objects.filter(numero_camada=numero_camada)

            # Si el curso ya existía, mostrar mensaje de error
            if curso_existente.exists():
                error_message = "Error: Este curso ya existe en la base de datos."
                return render(request, 'MiSitio/agregar_curso.html', {'form': form, 'error_message': error_message})

            # Guardar el formulario sin el campo 'verificado' para evitar problemas con el modelo
            curso = form.save(commit=False)

            # Guardar el campo 'verificado' con el valor predeterminado (False)
            curso.verificado = form.cleaned_data['verificado']
            curso.save()

            return redirect('agregar_curso')  # Puedes crear esta vista después

    else:
        form = CursoForm()

    return render(request, 'MiSitio/agregar_curso.html', {'form': form})

def agregar_estudiantes(request):
    if request.method == 'POST':
        form = EstudiantesForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Verificar si el profesor ya existe por email
            estudiantes_existente = Estudiantes.objects.filter(email=email).exists()

            # Si el profesor ya existía, mostrar mensaje de error
            if estudiantes_existente:
                error_message = "Error: Este email ya existe en la base de datos."
                return render(request, 'MiSitio/agregar_estudiantes.html', {'form': form, 'error_message': error_message})

            form.save()
            return redirect('agregar_estudiantes')
    else:
        form = EstudiantesForm()

    return render(request, 'MiSitio/agregar_estudiantes.html', {'form': form})