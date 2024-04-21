from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

from .models import Curso, Tutor, Alumno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nombre', 'curso']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'numero_camada']