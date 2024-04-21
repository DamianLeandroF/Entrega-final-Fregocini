from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path('agregar-curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar-tutor/', views.agregar_tutor, name='agregar_tutor'),
    path('agregar-alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('veralumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('vercursos/', views.lista_cursos, name='lista_cursos'),
    path('vertutores/', views.lista_tutores, name='lista_tutores'),
    path('buscar_alumnos/', views.buscar_alumnos, name='buscar_alumnos'),
    path('buscar_profesores/', views.buscar_profesores, name='buscar_profesores'),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path('edita_curso/<int:id>/', views.edita_curso, name='edita_curso'),

    path("elimina_alumnos/<int:id>", views.elimina_alumno, name='elimina_alumno'),
    path("edita_alumnos/<int:id>", views.edita_alumno, name='edita_alumno'),

    path("elimina_profesor/<int:id>", views.elimina_profesor, name='elimina_profesor'),
    path("edita_profesor/<int:id>", views.edita_profesor, name='edita_profesor'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),

]

