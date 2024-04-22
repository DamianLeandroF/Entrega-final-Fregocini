from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Tutor, Alumno
from .forms import CursoForm, TutorForm, AlumnoForm
def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def alumnos(request):
    return render(request , "alumnos.html")






def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")



def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'veralumnos.html', {'alumnos': alumnos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'vercursos.html', {'cursos': cursos})

def lista_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'vertutores.html', {'tutores': tutores})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})

def agregar_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TutorForm()
    return render(request, 'agregar_tutor.html', {'form': form})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})



def buscar_alumnos(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
    else:
        alumnos = []
    return render(request, 'buscar_alumnos.html', {'alumnos': alumnos})

def buscar_profesores(request):
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        profesores = Tutor.objects.filter(nombre__icontains=nombre)
    else:
        profesores = []
    return render(request, 'buscar_profesores.html', {'profesores': profesores})

def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('lista_cursos')

def edita_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':

        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():

            form.save()

            return redirect('lista_cursos')
    else:
 
        form = CursoForm(instance=curso)


    return render(request, 'edita_curso.html', {'form': form})


def elimina_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    alumno.delete()

    return redirect('lista_alumnos')


def edita_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':

        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():

            form.save()

            return redirect('lista_alumnos')
    else:

        form = AlumnoForm(instance=alumno)


    return render(request, 'edita_alumno.html', {'form': form})

def elimina_profesor(request, id):
    profesor = get_object_or_404(Tutor, id=id)

    profesor.delete()

    return redirect('lista_tutores')

def edita_profesor(request, id):
    profesor = get_object_or_404(Tutor, id=id)
    
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('lista_tutores')
    else:
        form = TutorForm(instance=profesor)

    return render(request, 'edita_profesor.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


